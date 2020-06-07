import numpy as np
from pysndfx import AudioEffectsChain
import types
import globals
import threading

def getModifiedSound(vocalProfile):
  funcs = []
  for key, value in __import__(__name__).__dict__.items():
      if type(value) is types.FunctionType:
        funcs.append(value)
  for fun in funcs:
    if globals.profiles[vocalProfile-1][3] == str(fun).split(' ')[1]:
      print("in for fun in funcs")
      print("fun: ", fun)
      audio = threading.Thread(target=fun, args=())
      audio.start()

def No_Effect():
  return 1

def Chipmunk():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  fx = (AudioEffectsChain()
        .pitch(shift=(default * 200), segment=82, search=14.68, overlap=12)
        (None, None, channels_out=1)
      )
  return

def SpaceMan():
  fx = (AudioEffectsChain()
        .pitch(shift=150, segment=82, search=14.68, overlap=12)
        .phaser(gain_in=0.6, gain_out=0.8, delay=2, decay=0.75, triangular=True)
        (None,None,channels_out=1))
  return

def Evil():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  fx = (AudioEffectsChain()
        .pitch(shift=(default * -100), segment=82, search=14.68, overlap=12)
        (None, None, channels_out=1)
       )
  return

def Megaphone():
  fx = (AudioEffectsChain()
        .overdrive(gain=37, colour=1)        
        (None, None, channels_out=1)
       )
  return

def Dim_Sound():
  fx = (AudioEffectsChain()
        .lowpass(frequency=450, q=0.707)
        .lowshelf(gain=-20.0, frequency=300, slope=0.5)
        (None, None, channels_out=1)
       )
  return

def Chorus():
  chorus1 = [50, 0.4, 0.25, 2, 't']
  chorus2 = [60, 0.32, 0.4, 2.3, 't']
  chorus3 = [40, 0.3, 0.3, 1.3, 's']
  decays = list((chorus1, chorus2, chorus3))
  fx = (AudioEffectsChain()
        .chorus(gain_in=0.8, gain_out=0.5, decays=decays)
        (None, None, channels_out=1)
       )
  return 

def Echo():
  fx = (AudioEffectsChain()
        .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
        (None, None, channels_out=1)
       )
  return

def Cave():
  fx = (AudioEffectsChain()
        .reverb(reverberance=100, hf_damping=50,room_scale=100, stereo_depth=100, pre_delay=20, wet_gain=0, wet_only=False) 
        (src=None, dst=None, channels_out=1)
       )
  return

def Harmony():
  fx1 = (AudioEffectsChain()
         .pitch(shift=500, segment=82, search=14.68, overlap=12)
         (None, None, channels_out=1)
        )
  print("after fx1")
  fx2 = (AudioEffectsChain()
         .pitch(shift=500, segment=82, search=14.68, overlap=12)
         (None, None, channels_out=1)
        )
  print("after fx2")
  root = fx1()
  print("root shape: ", root.shape)
  third = fx2()
  print("third shape: ", third.shape)
  outdata = np.add(root, third)
  print("outdata shape: ", outdata.shape)
  return