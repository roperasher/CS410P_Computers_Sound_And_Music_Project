import numpy as np
import globals
from pysndfx import AudioEffectsChain
import fxHandler

def getModifiedSound(vocalProfile, indata):
  if vocalProfile == 1:
    return noEffect(indata)
  if vocalProfile == 2:
    return pitchbend(indata)
  if vocalProfile == 3:
    return testingPysndfx(indata)

def noEffect(indata):
  return indata

def pitchbend(indata):
  shift = 20 
  left, right = indata[0::2], indata[1::2]  # left and right channe
  lf, rf = np.fft.rfft(left), np.fft.rfft(right)
  lf, rf = np.roll(lf, shift), np.roll(rf, shift)
  lf[0:shift], rf[0:shift] = 0, 0
  nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
  ns = np.concatenate((nl, nr), axis=0)
  return ns 

def testingPysndfx(indata):
  fx = (AudioEffectsChain().pitch(-600))
  outdata = fxHandler.pitchHandler(fx(indata))
  return outdata 