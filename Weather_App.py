import requests
import json 
import pyttsx3
import os 

engine = pyttsx3.init()
engine.setProperty("rate",130)

city = input("Enter the City Name = ")

API_KEY = os.environ.get("OPENWEATHER_API", "ad3f8c9581d17481dcf21e53b11c9d8e")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}"


try:
    r = requests.get(url, timeout = 10)
except requests.exceptions.RequestException as e:
    print(f"Network Error : {e}")
    exit()
    
try :
    wdic = r.json()

except ValueError:
    print("Error : Invalid reponse from API")
    exit()

cod = wdic.get("cod")
# OpenWeather may return "cod" as string on errors
if isinstance(cod, str):
    try:
        cod = int(cod)
    except ValueError:
        cod = None

if cod != 200:      # If it is not 200 then it is an error
    print(f"Error : {wdic.get('message','City not Found')}")
    exit()

def climate():
    Weather = (wdic["weather"][0]["main"])          # we use 0 due to it is a list other is dictionary
    C_statement = f"The Weather is {Weather} in {city}"
    print(C_statement)
    engine.say(C_statement)
    engine.runAndWait()

def Temp():
    ktemp = (wdic["main"]["temp"])
    ktemp = int(ktemp - 273)
    T_statement = f"The Temperature is {ktemp}°C in {city}"

    print(T_statement)
    engine.say(T_statement)
    engine.runAndWait()

def Feels_Like():
    Ftemp = (wdic["main"]["feels_like"])
    Ftemp = int(Ftemp - 273)
    F_statement = f"The Feels Like Temperature is {Ftemp}°C in {city}"
    print(F_statement)
    engine.say(F_statement)
    engine.runAndWait()

def Visibility():
    Visible = (wdic["visibility"])
    Visible = Visible/1000
    V_statement = f"The Visibility is {Visible}Km in {city}"

    print(V_statement)
    engine.say(V_statement)
    engine.runAndWait()


climate()
Temp()
Feels_Like()
Visibility()
wish = ("\nThank You!...")
print(wish)
engine.say(wish)
engine.runAndWait()
