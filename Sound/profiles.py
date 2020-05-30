import numpy as np
from pysndfx import AudioEffectsChain
import fxHandler
import types

def getModifiedSound(vocalProfile, indata):
  funcs = []
  for key, value in __import__(__name__).__dict__.items():
      if type(value) is types.FunctionType:
        funcs.append(value)
  return funcs[vocalProfile](indata)

def No_Effect(indata):
  return indata

def Chipmunk(indata):
  fx = (AudioEffectsChain()
          .pitch(shift=1000, segment=82, search=14.68, overlap=12)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.pitchHandler(modifiedSound)
  return outdata

def Evil(indata):
  fx = (AudioEffectsChain()
        .pitch(shift=-500, segment=82, search=14.68, overlap=12)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.pitchHandler(modifiedSound)
  return outdata

def Megaphone(indata):
  fx = (AudioEffectsChain()
        .overdrive(gain=37, colour=1)        
        )
  modifiedSound = fx(indata)
  outdata = fxHandler.pitchHandler(modifiedSound)
  return outdata

def TriedToMake_UnderwaterSound_ButItJustSoundLikeImBehindAWall(indata):
  fx = (AudioEffectsChain()
        .lowpass(frequency=450, q=0.707)
        .lowshelf(gain=-20.0, frequency=300, slope=0.5)
       )
  modifiedSound = fx(indata)
  outdata = fxHandler.lowpassHandler(modifiedSound)
  return outdata

# currently doesn't error out, but doesn't actually add chorus effect
def Chorus_Not_Currently_Working(indata):
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

'''
def cave(indata):
  fx = (AudioEffectsChain()
        .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
       )
  modifiedSound = fx(indata)
  print("modified sound size: ", modifiedSound.size)
  print("modified sound shape: ", modifiedSound.shape)
  outdata = fxHandler.pitchHandler(modifiedSound)
  print("outdata size: ", outdata.size)
  print("outdata shape: ", outdata.shape)
  return modifiedSound 
'''


