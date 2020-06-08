# VocalSoX
# Spring 2020 CS410P Computers Sound And Music Project

Contributors:
  - Asher Roper - roper@pdx.edu
  - Jordan Co - cojor@pdx.edu
  - Alexander Wallace - ajw29@pdx.edu

Project Title:
  - VocalSoX

Project:

Our program is a real time voice modifier. It contains various vocal profiles that run a single or series of sound effects on real time audio.

Build Instructions:

  1. Compatible Platforms
    - Linux
    - MacOS
  Not Compatible With:
    - Windows

  2. External Libraries
    - pysndfx
      $pip3 install pysndfx
    - SoX
      $apt install sox
    - sounddevice
      $pip3 install sounddevice --user
    - tkinter
      $pip3 install tkinter
    - psutil
      $pip3 install psutil

  3. Running our program
    From the root directory, run the following command:
    $python3 main.py

  4. How to use the GUI
    Select a vocal profile, then click the “Start/Stop” button. This will instantiate a real time audio stream and modify your voice based on the profile you selected. Clicking on another profile will allow you to change to that profile automatically

    Creating a profile means to make a new vocal profile based on a profile that already exists. Currently, this only works for “Chipmunk” and “Evil” which are effects that raise and lower the pitch. In the “Effect Name” box, enter the name of the new vocal profile you would like to create. In the “Level(1-10)” box, enter the strength of the effect that you want, with the default being level 5. Then click “Add New Profile” and your profile will be appended to the bottom of the list of effects.

    The “Microphone” and “Speaker” selection boxes currently do not work. They functioned properly in an older version of our project. This was created to connect our computer microphone and speaker to applications like Zoom and Discord. However, when we did an 

Testing:

Our test file is ~/testExamples/fx.py
Since our initial problem was getting the vocal profiles to work in real time, we used fx.py to check to see if the profiles worked when applying to audio files. The results of the test are in ~/testExamples as:
  - fx.wav
  - test.wav
  - voiceTest.wav

What worked? What didn't? How satisfied are you with the result? What would you like to improve in the future?

  We were able to create a real time audio stream. We first tested effects and later applied it to the stream. We setup a GUI to allow a user to change profiles quickly. A feature later was added to create more profiles based on the existing effects to add different parameters. 

  Most of our efforts for the project went into dealing with the real time audio. We initially used sounddevice to work with the real time audio input and output. This seemed like the right approach at first, but we were never able to get a clear audio stream using this method. Very late into the project, we found that pysndfx (but really SoX) actually supported real time audio input, modification, and output. With their library, we were able to get near perfect audio modification in real time with close to no latency. Once discovering this workaround, we decided to scrap the use of sounddevice for real time audio altogether. 

  We were able to get the system devices and allow the user to select them. This feature needed to be reworked due to an update which would take us some more time. Some effects we were not able to obtain an ideal profile for such as an underwater effect. Our team was working on 3 different operating systems and some of us were able to install a virtual audio port and connect it to applications like zoom and skype. Since we updated the stream process, directing to the virtual audio port will need an update as well. Our team ended up using a python library for an operating system command to kill the audio stream process. We intended to change this feature to cut the stream without this workaround.

  We are satisfied with how the effects turned out. Because of the update, the quality of the audio and effects have vastly improved. If we have the time in the future we would like to add more features to the GUI and lots more effects such as autotune, DJ, and harmonizer.
