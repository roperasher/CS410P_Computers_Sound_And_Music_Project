# This script test the pysndfx code on a simple 440hz sine wav file

# Import the package and create an audio effects chain function.
from pysndfx.dsp import AudioEffectsChain
import numpy as np
import os.path
from scipy import signal
from scipy.io.wavfile import read, write
import sounddevice as sd


fx = (
    AudioEffectsChain()
    .highshelf()
    #.reverb()
    #.phaser()
    #.delay()
    #.lowshelf()
)

def genTestWav():
    frequency = 440  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 3  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi).astype(np.float32)
    write('test.wav', fs, note)

def recordTestWav():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('voiceTest.wav', fs, myrecording)  # Save as WAV file 

# Read in sample file for effect processing 
def main():

    # Run test with 440hz sine wave file
    # if (os.path.exists('test.wav')) is False:
    #     genTestWav()

    # infile = 'test.wav' # float32
    recordTestWav()
    infile = 'voiceTest.wav'
    outfile = 'fx.wav'
    sample_rate, sample_data = read(infile)

    print('input shape: ', sample_data.shape)
    y = fx(sample_data)
    print('top 20 of output: ', y[:20])
    print('output shape: ', y.shape)
    write(outfile, 44100, y)

main()