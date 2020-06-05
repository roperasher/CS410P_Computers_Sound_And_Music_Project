# reformats numpy array after running sine wave through a vocal effect

import numpy as np
import globals

sampleRate = 2048

# notes on how fx modify numpy array shape and size
'''
No change:
  - pitch()
  - overdrive()
  - lowpass()
  - highpass()

Change:
  - chorus()
  - reverb()
'''

# reformat numpy array for pitch()
def pitchHandler(sineWave):
  return sineWave
  return np.ravel(sineWave, order='F').reshape(-1, 1)[:sampleRate]

# reformat numpy array for overdrive()
def overdriveHandler(sineWave):
  return pitchHandler(sineWave)

def lowpassHandler(sineWave):
  return pitchHandler(sineWave)

# reformat numpy array for chorus()
# currently doesn't error out, but doesn't actually add chorus effect
def chorusHandler(sineWave):
  return pitchHandler(sineWave)


