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
    #.highshelf()
    #.reverb()
    .phaser(decay=0.5, triangular=True)
    #.pitch(-1000)
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
    note = np.sin(frequency * t * 2 * np.pi).astype(np.int16)
    write('test.wav', fs, note)

def recordTestWav():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    
    print("***** RECORDING ******")
    myrecording = sd.rec(
        int(seconds * fs), 
        samplerate=fs, 
        channels=1,
        dtype=np.int16,
        blocking=True)
    sd.wait()  # Wait until recording is finished
    write('voiceTest.wav', fs, myrecording)  # Save as WAV file 

# Read in sample file for effect processing 
def main():

    # Run test with 440hz sine wave file
    # if (os.path.exists('test.wav')) is False:
    #     genTestWav()

    # infile = 'test.wav' # float32

    if (os.path.exists('voiceTest.wav')) is False:
        recordTestWav()
    infile = 'voiceTest.wav'
    outfile = 'fx.wav'
    sample_rate, sample_data = read(infile)

    print('input shape: ', sample_data.shape)
    print(sample_data[:10])
    y = fx(sample_data)
   # print('top 20 of output: ', y[:20])
    #y = np.swapaxes(y, 0, 1)
    print('output shape: ', y.shape)
    print(y[:10])
    write(outfile, 44100, y)

main()