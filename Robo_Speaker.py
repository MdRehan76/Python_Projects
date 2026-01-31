import pyttsx3

print("Welcome to RoboSpeaker!... Created by rehan")
engine = pyttsx3.init()
engine.setProperty("rate",130)  #Speaking Speed
print("Enter 'Q' to exit" )
while True:
    x = input("Enter what you want to speak : ")

    if x.upper() == "Q":
        print("Good Bye my Friend !...Come Soon")
        engine.say("Good Bye my Friend !...Come Soon")
        engine.runAndWait()
        break

    engine.say(x)
    engine.runAndWait()
