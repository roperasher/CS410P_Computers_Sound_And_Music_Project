import numpy as np
import globals
from pysndfx import AudioEffectsChain
import fxHandler

def getModifiedSound(vocalProfile, indata):
  if vocalProfile == 1:
    return noEffect(indata)
  if vocalProfile == 2:
    return pitchBendUp(indata)
  if vocalProfile == 3:
    return pitchBendDown(indata)
  if vocalProfile == 4:
    return chorusEffect(indata)

def noEffect(indata):
  return indata

def pitchBendUp(indata):
  fx = (AudioEffectsChain()
          .pitch(shift=800, segment=82, search=14.68, overlap=12)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.pitchHandler(modifiedSound)
  return outdata

def pitchBendDown(indata):
  fx = (AudioEffectsChain()
        .pitch(shift=-600, segment=82, search=14.68, overlap=12)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.pitchHandler(modifiedSound)
  return outdata

# currently doesn't error out, but doesn't actually add chorus effect
def chorusEffect(indata):
  chorus1 = [50, 0.4, 0.25, 2, 't']
  chorus2 = [60, 0.32, 0.4, 2.3, 't']
  chorus3 = [40, 0.3, 0.3, 1.3, 's']
  decays = list((chorus1, chorus2, chorus3))
  fx = (AudioEffectsChain()
        .chorus(gain_in=0.8, gain_out=0.5, decays=decays)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.chorusHandler(modifiedSound)
  return outdata
