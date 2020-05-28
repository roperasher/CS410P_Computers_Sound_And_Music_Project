#CS410P_Computers_Sound_And_Music_Project
#Asher Roper
#Jordan Co
#Alexander Wallace

import wire
import profiles
import globals 

def main():
  while (True):
    print("Vocal profiles:")
    print("1. No effect")
    print("2. Pitch bend up")
    print("3. Pitch bend down")
    print("4. Chorus effect")
    userInput = input("Enter a value: ")
    globals.vocalProfile = int(userInput)
    wire.startStream()

if __name__ == "__main__":
  main()
