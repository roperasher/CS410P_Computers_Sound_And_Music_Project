import threading
import numpy as np
from pysndfx import AudioEffectsChain
import types
import globals

def getModifiedSound(vocalProfile):
  funcs = []
  for key, value in __import__(__name__).__dict__.items():
      if type(value) is types.FunctionType:
        funcs.append(value)
  for fun in funcs:
    if globals.profiles[vocalProfile-1][2] == str(fun).split(' ')[1]:
      audio = threading.Thread(target=fun, args=())
      audio.start()

def No_Effect():
  (AudioEffectsChain()
    .gain(db=0)
    (src=None, dst=None, channels_out=1)
  )

def Chipmunk():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  (AudioEffectsChain()
    .pitch(shift=(default * 200), segment=82, search=14.68, overlap=12)
    (src=None, dst=None, channels_out=1)
  )

def Evil():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  (AudioEffectsChain()
    .pitch(shift=(default * -100), segment=82, search=14.68, overlap=12)
    (src=None, dst=None, channels_out=1)
  )

def SpaceMan():
  (AudioEffectsChain()
    .pitch(shift=150, segment=82, search=14.68, overlap=12)
    .phaser(gain_in=0.6, gain_out=0.8, delay=2, decay=0.75, triangular=True)
    (src=None, dst=None,channels_out=1)
  )

def Cave():
  (AudioEffectsChain()
    .reverb(reverberance=100, hf_damping=50,room_scale=100, stereo_depth=100, pre_delay=20, wet_gain=0, wet_only=False) 
    (src=None, dst=None, channels_out=1)
  )

def Cave_Echo():
  (AudioEffectsChain()
    .reverb(reverberance=100, hf_damping=50,room_scale=100, stereo_depth=100, pre_delay=20, wet_gain=0, wet_only=False) 
    .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
    (src=None, dst=None, channels_out=1)
  )

def Megaphone():
  (AudioEffectsChain()
    .overdrive(gain=37, colour=1)        
    (src=None, dst=None, channels_out=1)
  )

def Wall():
  (AudioEffectsChain()
    .lowpass(frequency=450, q=0.707)
    .lowshelf(gain=-20.0, frequency=300, slope=0.5)
    (src=None, dst=None, channels_out=1)
  )

def Robot():
  chorus1 = [50, 0.4, 0.25, 2, 't']
  chorus2 = [60, 0.32, 0.4, 2.3, 't']
  chorus3 = [40, 0.3, 0.3, 1.3, 's']
  decays = list((chorus1, chorus2, chorus3))
  (AudioEffectsChain()
    .pitch(shift=-300, segment=82, search=14.68, overlap=12)
    .overdrive(gain=25, colour=1)        
    .chorus(gain_in=0.9, gain_out=1.2, decays=decays)
    .phaser(gain_in=0.6, gain_out=0.8, delay=2, decay=.90, triangular=True)
    (src=None, dst=None, channels_out=1)
  )

def Echo():
  (AudioEffectsChain()
    .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
    (src=None, dst=None, channels_out=1)
  )