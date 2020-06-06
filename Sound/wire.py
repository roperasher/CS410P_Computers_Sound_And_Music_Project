#!/usr/bin/env python3

"""Pass input directly to output.
See https://www.assembla.com/spaces/portaudio/subversion/source/HEAD/portaudio/trunk/test/patest_wire.c
sound device docs - https://python-sounddevice.readthedocs.io/en/latest/api/index.html
"""
import argparse
import logging
import numpy as np
import sounddevice as sd
import profiles
from scipy.interpolate import interp1d
import globals

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
# optional, only if using non default device
parser.add_argument('-i', '--input-device', type=int_or_str, help='input device ID or substring')
parser.add_argument('-o', '--output-device', type=int_or_str, help='output device ID or substring')
# channels for stream call back function
parser.add_argument('-c', '--channels', type=int, default=1, help='number of channels')
# types - float32, int32, int16, int8, uint8
parser.add_argument('-t', '--dtype', default=np.int16, help='audio data type')
# input output sampling frequency
parser.add_argument('-s', '--samplerate', type=int, default=44100, help='sampling rate')
# number of frames passed to call back function
parser.add_argument('-b', '--blocksize', type=int, default=2048, help='block size')
# latency setting for i/o devices
parser.add_argument('-l', '--latency', type=float, default=0.5, help='latency in seconds')
args = parser.parse_args()

# Can manipulate sound blocks here!!
def callback(indata, outdata, frames, time, status):
    """
        indata(ndarray): input buffer
        outdata(ndarray): output buffer
        Call back for portaudio to periodically poll input and output channels. 
        Currently this callback function simply forwards input to the output.
    """
    if status:
        print(status)
    #TODO try using queue for blocks larger than block size, chop up into block size and pad zeros, enqueue. Dequeue chunk and set to outdata
    outdata[:] = profiles.getModifiedSound(globals.vocalProfile, indata)
    # commented this out since numpy array reshaping happens within each function in profiles.py
    '''
    # Can manipulate sound blocks here!!
    # print("~~indata~~")
    # print(indata.shape)
    # print(indata[:5])
    #out = profiles.getModifiedSound(globals.vocalProfile, indata)
    # print("~~outdata~~")
    # combine L/R channels and reshape, (1024,2) --> (2048,1)
    #out = np.ravel(out, order='F').reshape(-1,1)[:frames]
    # print(out.shape)
    # print(out[:5])
    #outdata[:] = out
    '''

def startStream():
    stream = sd.Stream(device=(globals.mic, globals.speaker), # "CABLE Input (VB-Audio Virtual C, MME"
                samplerate=args.samplerate, blocksize=args.blocksize,
                dtype=args.dtype, latency=args.latency,
                channels=args.channels, callback=callback)
    stream.start()
    return stream
