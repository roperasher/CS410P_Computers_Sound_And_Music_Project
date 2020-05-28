import numpy as np
import globals
from pysndfx import AudioEffectsChain

np.set_printoptions(threshold=30)


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
  shift = 100 
  left, right = indata[0::2], indata[1::2]  # left and right channe
  lf, rf = np.fft.rfft(left), np.fft.rfft(right)
  lf, rf = np.roll(lf, shift), np.roll(rf, shift)
  lf[0:shift], rf[0:shift] = 0, 0
  nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
  ns = np.concatenate((nl, nr), axis=0)
  return ns 

def testingPysndfx(indata):

  chorus1 = [50, 0.4, 0.25, 2, 't']
  chorus2 = [60, 0.32, 0.4, 2.3, 't']
  chorus3 = [40, 0.3, 0.3, 1.3, 's']
  decays = list((chorus1, chorus2, chorus3))
  print(type(decays))
  fx = (
    AudioEffectsChain()
    .chorus(gain_in=0.8, gain_out=0.5, decays=decays)
    .pitch(-300)
    #.highshelf()
    #.reverb()
    #.phaser(decay=0.5, triangular=True)
    #.delay()
    #.lowshelf()
  )
  
  outdata = fx(indata)
  #print("indata type: ", type(indata))
  #print("indata size: ", indata.size)
  #print("input shape: ", indata.shape)
  #print("indata: ", indata)
  #print("outdata type: ", type(outdata))
  #print("outdata size: ", outdata.size)
  #print("outdata shape: ", outdata.shape)
  #print("outdata: ", outdata)
  #outdata = np.stack((outdata[0], outdata[1]), axis=1)
  #outdata = np.swapaxes(outdata, 0, 1)
  return outdata 