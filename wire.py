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
import queue
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
parser.add_argument('-b', '--blocksize', type=int, default=0, help='block size')
# latency setting for i/o devices
parser.add_argument('-l', '--latency', type=float, default=0.5, help='latency in seconds')
args = parser.parse_args()

q = queue.Queue()

def chopAndEnqueue(data, outdata, frames):
    # Shit don't work
    padding = frames - (data.size % frames)
    padded = np.pad(data, (0,padding), 'constant')
    reshaped = padded.reshape(padded.size//frames, frames)

    for arr in reshaped:
        outdata[:] = arr
        q.put_nowait(arr)
    
#TODO try using separate Input Stream and Output Stream instead Stream object.
def callback(indata, outdata, frames, time, status):
    """
        indata(ndarray): input buffer
        outdata(ndarray): output buffer
        Call back for portaudio to periodically poll input and output channels. 
        Currently this callback function simply forwards input to the output.
    """
    if status:
        print(status)

    print("frames: ", frames)
    print("~~indata~~")
    print(indata.shape)
    data = profiles.getModifiedSound(globals.vocalProfile, indata)
    print("data shape: ", data.shape)
    data = np.ravel(data, order='F').reshape(-1,1)
    print("after ravel: ", data.shape)

    size = data.size
    print("Size: ", size)

# SHIT DON"T WORK
    if size == frames:
        outdata[:] = data
    elif size > frames:
        print("*** Data size is larger than frame size ****")
        padding = frames - (size % frames)
        print("padding: ", padding)
        print("data shape: ", data.shape)
        data = np.pad(data, (0,padding), 'constant')
        reshaped = data.reshape(data.size//frames, frames)
        for arr in reshaped:
            outdata[:] = arr.reshape(-1,1)

            print("~~outdata~~")
            print(outdata.shape)
    else:
        print("*** Data size is smaller than frame size ****")
        data = np.pad(data, (0, frames - size), 'constant')
        outdata[:] = data
        
    #chopAndEnqueue(data, outdata, frames)

    # if(q.empty()):
    #     outdata.fill(0)
    # else:
    #     outdata[:] = q.get_nowait().reshape(-1,1)

    # print("~~outdata~~")
    # print(outdata.shape)


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

if __name__ == '__main__':
    startStream()