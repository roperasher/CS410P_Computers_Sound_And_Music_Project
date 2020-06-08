# profiles.py is where are the vocal profiles are stored
# each function is a vocal profile, which adds some sort of sound effect to audio
# every profile instantiates a sox process that takes, modifies, and outputs audio in real time

import threading
import numpy as np
from pysndfx import AudioEffectsChain
import types
import globals

# gets the requested vocal profile and envokes it in a separate thread called "audio"
def getModifiedSound(vocalProfile):
  funcs = []
  for key, value in __import__(__name__).__dict__.items():
      if type(value) is types.FunctionType:
        funcs.append(value)
  for fun in funcs:
    if globals.profiles[vocalProfile-1][2] == str(fun).split(' ')[1]:
      audio = threading.Thread(target=fun, args=())
      audio.start()

# default profile 
# doesn't modify audio in any way
def No_Effect():
  (AudioEffectsChain()
    .gain(db=0)
    (src=None, dst=None, channels_out=1)
  )

# chipmunk vocal profile
# takes audio and pitch shifts it extremely high
# can use this to create a new profile in the GUI of varying pitches. Level(1-10)
def Chipmunk():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  (AudioEffectsChain()
    .pitch(shift=(default * 200), segment=82, search=14.68, overlap=12)
    (src=None, dst=None, channels_out=1)
  )

# evil vocal profile
# takes audio and pitch shifts it very low
# can use this to create a new profile in the GUI of varying pitches. Level(1-10)
def Evil():
  default = int(globals.profiles[globals.vocalProfile-1][0])
  if default == 0:
    default = 5
  (AudioEffectsChain()
    .pitch(shift=(default * -100), segment=82, search=14.68, overlap=12)
    (src=None, dst=None, channels_out=1)
  )

# spaceman vocal profile
# pitch shifts audio then runs audio through a phaser
def SpaceMan():
  (AudioEffectsChain()
    .pitch(shift=150, segment=82, search=14.68, overlap=12)
    .phaser(gain_in=0.6, gain_out=0.8, delay=2, decay=0.75, triangular=True)
    (src=None, dst=None,channels_out=1)
  )

# cave vocal profile
# adds a lot of reverb to audio
def Cave():
  (AudioEffectsChain()
    .reverb(reverberance=100, hf_damping=50,room_scale=100, stereo_depth=100, pre_delay=20, wet_gain=0, wet_only=False) 
    (src=None, dst=None, channels_out=1)
  )

# cave_echo vocal profile
# adds a lot of reverb to audio as well as a delay (echo)
def Cave_Echo():
  (AudioEffectsChain()
    .reverb(reverberance=100, hf_damping=50,room_scale=100, stereo_depth=100, pre_delay=20, wet_gain=0, wet_only=False) 
    .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
    (src=None, dst=None, channels_out=1)
  )

# megaphone vocal profile
# adds overdrive to audio to emulate megaphone like sound 
def Megaphone():
  (AudioEffectsChain()
    .overdrive(gain=37, colour=1)        
    (src=None, dst=None, channels_out=1)
  )

# wall vocal profile
# adds a lowpass and lowshelf filter to audio
# boosts low and cuts high frequencies to emulate the sound of someone in another room
def Wall():
  (AudioEffectsChain()
    .lowpass(frequency=450, q=0.707)
    .lowshelf(gain=-20.0, frequency=300, slope=0.5)
    (src=None, dst=None, channels_out=1)
  )

# robot vocal profile
# adds pitch shifter, overdrive, chorus, and phaser effect to audio
# tries to emulate robot sound
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

# regular_echo vocal profiles
# echos regular audio 3 times
def Regular_Echo():
  (AudioEffectsChain()
    .delay(gain_in=0.8, gain_out=0.5, delays=list((1000, 1800)), decays=list((0.3, 0.25)), parallel=False)
    (src=None, dst=None, channels_out=1)
  )