# This script test the pysndfx code on a simple 440hz sine wav file

# Import the package and create an audio effects chain function.
from pysndfx import AudioEffectsChain
import numpy as np
from scipy import signal
from scipy.io.wavfile import read, write


fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
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


# Read in sample file for effect processing 
def main():
    infile = 'test.wav' # float32
    outfile = 'fx.wav'
    sample_rate, sample_data = read(infile)
    y = fx(sample_data)
    write(outfile, 44100, y)

main()