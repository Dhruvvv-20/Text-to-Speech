import win32com.client as wincl

if __name__ == '__main__':
    print("Welcome to RoboSpeaker1.1 Created by Dhruv")
    speaker = wincl.Dispatch("SAPI.SpVoice")
    while True:
        x = input("Enter what you want me to speak (type 'exit' to stop): ")
        if x == 'exit':
            print("Exiting RoboSpeaker1.1. Goodbye!")
            speaker.Speak("Exiting RoboSpeaker1.1. Goodbye!")
            break
        
        speaker.Speak(x)
