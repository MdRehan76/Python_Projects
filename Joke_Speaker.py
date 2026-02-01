import pyjokes
import win32com.client

print("Welcome to Joke Speaker !... Have Fun")

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = -2  # Speed: -10 (slowest) to 10 (fastest), -2 is similar to rate 130

while True:
    try:
        n = int(input("Enter how many jokes to you want listen = "))
        if n > 0:
            break
        else:
            print("Please enter a positive Number.")
    except ValueError:
        print("Invalid Input! Please enter the positive integer")

for i in range(1,n+1):
    joke = pyjokes.get_joke()
    print(f"\n{i}. {joke}")
    speaker.Speak(joke)
    if i < n:
        x = input("If you want to Quit so press 'Q' or press any key to continue : ")
    
        if x.upper() == "Q":
            goodbye_msg = ("Thank You for listening Jokes,Be Happy")
            print(goodbye_msg+"😀😀")
            speaker.Speak(goodbye_msg)
            break
else:
    goodbye_msg = ("Thank You for listening Jokes,Be Happy")
    print(goodbye_msg+"😀😀")
    speaker.Speak(goodbye_msg)