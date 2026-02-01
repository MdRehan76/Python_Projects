import win32com.client

print("Welcome to RoboSpeaker!... Created by rehan")
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = -2 #Speaking Speed

print("Enter 'Q' to exit" )
while True:
    x = input("Enter what you want to speak : ")

    if x.upper() == "Q":
        print("Good Bye my Friend !...Come Soon")
        speaker.Speak("Good Bye my Friend !...Come Soon")
        break

    speaker.Speak(x)


