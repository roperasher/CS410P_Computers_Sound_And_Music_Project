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
parser.add_argument('-c', '--channels', type=int, default=2, help='number of channels')
# types - float32, int32, int16, int8, uint8
parser.add_argument('-t', '--dtype', default='int16', help='audio data type')
# input output sampling frequency
parser.add_argument('-s', '--samplerate', type=float, help='sampling rate')
# number of frames passed to call back function
parser.add_argument('-b', '--blocksize', type=int, default=1024, help='block size')
# latency setting for i/o devices
parser.add_argument('-l', '--latency', type=float, default=1, help='latency in seconds')
args = parser.parse_args()

def callback(indata, outdata, frames, time, status):
    """
        indata(ndarray): input buffer
        outdata(ndarray): output buffer
        Call back for portaudio to periodically poll input and output channels. 
        Currently this callback function simply forwards input to the output.
    """
    if status:
        print(status)
    # Can manipulate sound blocks here!!
    outdata[:] = profiles.getModifiedSound(globals.vocalProfile, indata) 

def startStream():
    try:
        with sd.Stream(device=(args.input_device, args.output_device),
                    samplerate=args.samplerate, blocksize=args.blocksize,
                    dtype=args.dtype, latency=args.latency,
                    channels=args.channels, callback=callback):
            print('#' * 80)
            print('press Return to select another vocal profile')
            print('#' * 80)
            input()
    except KeyboardInterrupt:
        parser.exit('\nInterrupted by user')
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))