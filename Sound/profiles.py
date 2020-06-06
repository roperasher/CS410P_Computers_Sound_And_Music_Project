import numpy as np
from pysndfx import AudioEffectsChain
import fxHandler
import types
import globals

def getModifiedSound(vocalProfile, indata):
  funcs = []
  for key, value in __import__(__name__).__dict__.items():
      if type(value) is types.FunctionType:
        funcs.append(value)
  for fun in funcs:
    if globals.profiles[vocalProfile-1][3] == str(fun).split(' ')[1]:
      return fun(indata)

def No_Effect(indata):
  return indata

def Chipmunk(indata):
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  fx = (AudioEffectsChain()
        .pitch(shift=(default * 200), segment=82, search=14.68, overlap=12)
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata

def SpaceMan(indata):
  fx = (AudioEffectsChain()
        .pitch(shift=150, segment=82, search=14.68, overlap=12)
        .phaser(gain_in=0.6, gain_out=0.8, delay=2, decay=0.75, triangular=True)
       (None,None,channels_out=1))
  outdata = fx(indata)
  return outdata


def Evil(indata):
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  fx = (AudioEffectsChain()
        .pitch(shift=(default * -100), segment=82, search=14.68, overlap=12)
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata

def Megaphone(indata):
  fx = (AudioEffectsChain()
        .overdrive(gain=37, colour=1)        
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata

def TriedToMake_UnderwaterSound_ButItJustSoundLikeImBehindAWall(indata):
  fx = (AudioEffectsChain()
        .lowpass(frequency=450, q=0.707)
        .lowshelf(gain=-20.0, frequency=300, slope=0.5)
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata

# currently doesn't error out, but doesn't actually add chorus effect
def Chorus_Not_Currently_Working(indata):
  chorus1 = [50, 0.4, 0.25, 2, 't']
  chorus2 = [60, 0.32, 0.4, 2.3, 't']
  chorus3 = [40, 0.3, 0.3, 1.3, 's']
  decays = list((chorus1, chorus2, chorus3))
  fx = (AudioEffectsChain()
        .chorus(gain_in=0.8, gain_out=0.5, decays=decays)
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata

def cave(indata):
  fx = (AudioEffectsChain()
        .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
        (None, None, channels_out=1)
       )
  outdata = fx(indata)
  return outdata 

