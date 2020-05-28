# reformats numpy array after running sine wave through a vocal effect

import numpy as np

sampleRate = 4096

# reformat numpy array for pitch()
def pitchHandler(sineWave):
  return np.ravel(sineWave, order='F').reshape(-1, 1)[:sampleRate]

# reformat numpy array for chorus()
# currently doesn't error out, but doesn't actually add chorus effect
def chorusHandler(sineWave):
  return pitchHandler(sineWave)
