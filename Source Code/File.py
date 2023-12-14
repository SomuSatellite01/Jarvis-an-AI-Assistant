

import sys
import time
import instaloader
import pywinauto
import requests
import pyjokes
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import os
import cv2
import webbrowser
import pywhatkit
import ttkbootstrap
import wikipedia
import subprocess
import smtplib
import pyautogui
from requests import get
engine =
pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Index 1 for British English
voice
# Text to speech
defspeak(audio):
engine.say(audio)
engine.runAndWait()

hour = datetime.datetime.now().hour
if 0 <= hour < 12:
speak("Good Morning!")
elif 12 <= hour < 18:
speak("Good Afternoon!")
else:
speak("Good Evening!")
speak("hello my lord am your jarvis tell how I can I be your
assistance")
def news(apikey):

url = f"https://newsapi.org/v2/top-
headlines?country=us&apiKey=ee478b9661ab43cc8f1c5c7ac676f6a1"

response = requests.get(url)
data = response.json()
if data["status"] == "ok":
articles = data["articles"]
for article in articles:
title = article["title"]
source = article["source"]["name"]
speak("Title: " + title)
speak("Source: " + source)
print(f"Title: {title}")
print(f"Source: {source}")
print(" ")
else:
print("Error occurred while fetching news.")

def takecommand():
r = sr.Recognizer()
with sr.Microphone() as source:
print("Listening...")
r.pause_threshold = 1
audio = r.listen(source, timeout=1, phrase_time_limit=5)
try:
print("Please wait, recognizing...")
query = r.recognize_google(audio, language='en-in')
print(f"User said: {query}")
if "stop" in query:
speak("Goodbye!")
return "stop"

except Exception as e:
speak("Say that again, please...")
return "none"
return query
#send email
def sendEmail(to, content):
server = smtplib.SMTP('localhost')
server.sendmail("", to, content)
server.quit()

if name == ' main ':
greet()
while True:
if 1:
query = takecommand().lower()
# Logic building for tasks
if "open notepad" in query:
os.startfile("notepad.exe")
elif "open command prompt" in query:
os.system("start cmd")
elif "camera" in query:
cap = cv2.VideoCapture(0)
while True:
# Capture frame-by-frame
ret, frame = cap.read()
# Display the resulting frame
cv2.imshow('Camera', frame)
# Check for 'q' key press to exit
if cv2.waitKey(1) == ord('q'):
break
# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
elif "music" in query:
speak("Playing Ed Sheeran songs on YouTube")
pywhatkit.playonyt("Ed Sheeran songs")
elif "ip address" in query:
ip = get('https://api.ipify.org').text
speak(f"your IP address is {ip}")

elif "wikipedia" in query:
speak("Searching Wikipedia...")
query = query.replace("wikipedia", "")
results = wikipedia.summary(query, sentences=2)
speak("According to Wikipedia")
speak(results)
print(results)
elif "youtube" in query:
speak("Opening YouTube")
webbrowser.open("https://www.youtube.com/")

elif "brave" in query:
speak("Opening Brave")

subprocess.Popen("C:\\Program Files\\BraveSoftware\\Brave-
Browser\\Application\\brave.exe")

elif "chrome" in query:
speak("Opening Chrome")
subprocess.Popen("C:\\Program
Files\\Google\\Chrome\\Application\\chrome.exe")

elif "firefox" in query:
speak("Opening Firefox")
subprocess.Popen("C:\\Program Files\\Mozilla
Firefox\\firefox.exe")

elif "edge" in query:
speak("Opening Edge")
subprocess.Popen("C:\\Program Files
(x86)\\Microsoft\\Edge\\Application\\msedge.exe")

elif "bing" in query:
speak("Opening Microsoft Bing")
webbrowser.open("https://www.bing.com/")
elif "google" in query:
speak("sir, What should I search on google")
cm = takecommand().lower()
webbrowser.open(f"{cm}")

elif "send message" in query:
speak("To whom do you want to send the message?")
recipient = takecommand().lower()
speak("What message do you want to send?")
message = takecommand()
pywhatkit.sendwhatmsg_instantly(f"+919652337951",
message)
elif "songs " in query:
speak("Which song do you want me to play")
msg = takecommand()
pywhatkit.playonyt(msg)
elif "email" in query:
#speak("What should I say?")
#content = takecommand().lower()
# to = 'finnumar@gmail.com'
#sendEmail(to, content)
#speak("Email has benn sent to Umar Farhan")
to_email = "finnumar@gmail.com"
email_content = "This is a test email sent without

authentication."

sendEmail(to_email, email_content)
except Exception as e:
print(e)
speak("sorry Email cant be sent am very sorry sir!")
elif "facebook" in query:
speak("Opening Facebook")
webbrowser.open("https://www.facebook.com/")
elif "instagram" in query:
speak("Opening Instagram")
webbrowser.open("https://www.instagram.com/")

elif "no thanks" in query:
speak("thanks for using me sir, have a great day")
sys.exit()
elif "close notepad" in query:
speak("Closing Notepad")
os.system("taskkill /f /im notepad.exe")
elif "close facebook" in query:
speak("Closing Facebook")
os.system("taskkill /f /im chrome.exe") # Assuming Facebook
is opened in Chrome
elif "close instagram" in query:
speak("Closing Instagram")
os.system("taskkill /f /im chrome.exe") # Assuming Instagram
is opened in Chrome
elif "close google" in query:
speak("Closing Google")
os.system("taskkill /f /im chrome.exe") # Assuming Google is opened in Chrome

elif "close brave" in query:
speak("Closing Brave")
os.system("taskkill /f /im brave.exe")
elif "close chrome" in query:
speak("Closing Chrome")
os.system("taskkill /f /im chrome.exe")
elif "close firefox" in query:
speak("Closing Firefox")
os.system("taskkill /f /im firefox.exe")
elif "close edge" in query:
speak("Closing Edge")
os.system("taskkill /f /im msedge.exe")
elif "close bing" in query:
speak("Closing Bing")
os.system("taskkill /f /im chrome.exe") # Assuming Bing is
opened in Chrome

elif "set alarm" in query:
speak("At what time should I set the alarm?")
alarm_time = takecommand().lower()
alarm_hour = int(alarm_time.split(":")[0])
alarm_minute = int(alarm_time.split(":")[1])
current_time = datetime.datetime.now()
alarm_time = datetime.datetime(
current_time.year,
current_time.month,
current_time.day,
alarm_hour,
alarm_minute,
0
)
if current_time > alarm_time:
alarm_time += datetime.timedelta(days=1) # Add 1 day if the alarm time has already passed today

time_difference = alarm_time - current_time
seconds = time_difference.total_seconds()
speak("Alarm has been set. I will notify you at the specified
time.")
datetime.time.sleep(seconds)
speak("Wake up! It's time!")
elif "jokes" in query:
joke = pyjokes.get_joke()
speak(joke)
elif "shutdown" in query:
speak("Are you sure you want to shutdown the computer?")
confirm = takecommand().lower()
if "yes" in confirm:
speak("Shutting down the computer")
os.system("shutdown /s /t 0")
else:
speak("Alright, I won't shutdown the computer")
elif "restart" in query:
speak("Are you sure you want to restart the computer?")
confirm = takecommand().lower()
if "yes" in confirm:
speak("Restarting the computer")
os.system("shutdown /r /t 0")
else:
speak("Alright, I won't restart the computer")
elif "sleep" in query or "go to sleep" in query:
speak("Putting the computer to sleep")
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

elif "tabs" in query:
# Get the active window handle
subprocess.Popen("code")
speak("Opening Visual Studio Code")
elif "news" in query:
speak("Please wait lord, fetching the latest news")
apikey = 'ee478b9661ab43cc8f1c5c7ac676f6a1'

news(apikey)
elif "weather" in query:
speak("Opening Weather window")
speak("Please type the name of the city you wanna search")
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

def get_weather(city):
API_key = "04b14c069ea7176786cd33daff091fac"
url =

f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API
_key}"

res = requests.get(url)
if res.status_code == 404:
messagebox.showerror("Error", "City not found")
return None
weather = res.json()
icon_id = weather['weather'][0]['icon']
temperature = weather['main']['temp'] - 273.15
description = weather['weather'][0]['description']
city = weather['name']
country = weather['sys']['country']
icon_url =

f"http://openweathermap.org/img/wn/{icon_id}@2x.png"

return (icon_url, temperature, description, city, country)

def search():
city = city_entry.get()
result = get_weather(city)
if result is None:
return
icon_url, temperature, description, city, country = result
location_label.configure(text=f"{city}, {country}")
image = Image.open(requests.get(icon_url,

stream=True).raw)

icon = ImageTk.PhotoImage(image)
icon_label.configure(image=icon)
icon_label.image = icon
temperature_label.configure(text=f"Temperature:

{temperature:.2f}°C")

description_label.configure(text=f"Description:

{description}")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
city_entry = tk.Entry(root, font="Helvetica 18")
city_entry.pack(pady=10)
search_button = tk.Button(root, text="Search",
command=search)
search_button.pack(pady=10)
location_label = tk.Label(root, font="Helvetica 25")
location_label.pack(pady=20)
icon_label = tk.Label(root)
icon_label.pack()
temperature_label = tk.Label(root, font="Helvetica 20")
temperature_label.pack()
description_label = tk.Label(root, font="Helvetica 20")
description_label.pack()
root.mainloop()
elif "dictionary" in query:
import tkinter as tk
from ttkbootstrap import Style, ttk
import requests

def get_definition(word):
response =

requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

if response.status_code == 200:
data = response.json()
if data:
meanings = data[0]['meanings']
definitions = [] # Corrected spelling
for meaning in meanings:
definitions.append(
f" Meaning:
{meaning['partOfSpeech']}\nDefinition:
{meaning['definitions'][0]['definition']}\n") # Corrected spelling

return '\n'.join(definitions)
return "No definitions found"

def search_definiton():
word = entry_word.get()
definition = get_definition(word)
text_output.configure(state = 'normal')
text_output.delete('1.0',tk.END)
text_output.insert(tk.END, definition)
text_output.configure(state = 'disabled')

root = tk.Tk()
style= Style(theme = 'flatly')
root.title("Dictionary App")
root.geometry("500x300")
#Search frame
frame_search = ttk.Frame(root)
frame_search.pack(padx=20, pady=20)
#Label for the word entry field
label_word = ttk.Label(frame_search, text = "Enter a words:",

font=('TkDefaultFont',15,'bold'))
label_word.grid(row = 0, column=0, padx=5, pady=5)
#Entry field for the word
entry_word = ttk.Entry(frame_search, width=20,
font=('TkDefaultFont 15'))
entry_word.grid(row=0, column=1, padx=5, pady=5)
#search Button
button_search = ttk.Button(frame_search, text= "Search",
command = search_definiton)
button_search.grid(row=0, column=2, padx=5, pady=5)

#Output frame
frame_output = ttk.Frame(root)
frame_output.pack(padx=20,pady=10)
#Text output field for displaying
text_output = tk.Text(frame_output, height=10, state='disabled',

font=('TkDefaultFont', 15))

text_output.pack()
root.mainloop()
elif "calender" in query:
from tkinter import ttk
import ttkbootstrap
#setup the window
root = ttkbootstrap.Window(themename= 'cyborg')
root.title('Calendar')
#function to get the date
def see_date():
date = cal.entry.get()
date_label.config(text=date)
#this is the DataEntry widget
cal = ttkbootstrap.DateEntry(root, dateformat = '%d/%m/%Y',
bootstyle = 'info')
cal.pack(padx=40, pady = 40)
#button to get the selected time

btn = ttk.Button(root, text="Show Date", bootstyle = "light-
outline", command=see_date)

btn.pack(padx=40, pady=45)
date_label = ttk.Label(root, text= "No date selected")
date_label.pack(padx=40, pady=50)
root.mainloop()
# elif "notes" or "note" in query:
# import tkinter as tk
# from tkinter import ttk, messagebox
# import json
# from ttkthemes import ThemedStyle
#
# # Create the main Window
# root = tk.Tk()
# root.title("Notes App")
# root.geometry("500x500")
#
# # Use ttkthemes for custom styles
# style = ThemedStyle(root)
# style.set_theme("equilux")
#
# # Create the notebook to hold the notes
# notebook = ttk.Notebook(root)
#
# # Load saved Notes
# notes = {}
# try:
# with open("notes.json", "r") as f:
# notes = json.load(f)
# except FileNotFoundError:
# pass
#
#
# # Create a function to add a new note
# def add_note():
# note_frame = ttk.Frame(notebook, padding=10)
# notebook.add(note_frame, text="New Note")
#
# title_label = ttk.Label(note_frame, text="Title:")
# title_label.grid(row=0, column=0, padx=10, pady=10,
sticky="W")
#
# title_entry = ttk.Entry(note_frame, width=40)
# title_entry.grid(row=0, column=1, padx=10, pady=10)
#
# content_label = ttk.Label(note_frame, text="Content:")
# content_label.grid(row=1, column=0, padx=10, pady=10,
sticky="W")

#
# content_entry = tk.Text(note_frame, width=40, height=10)
# content_entry.grid(row=1, column=1, padx=10, pady=10)
#
# # Create a function to save the notes
# def save_note():
# title = title_entry.get()
# content = content_entry.get("1.0", tk.END)
#
# # Add the notes to the dictionary
# notes[title] = content.strip()
#
# # Save the notes dictionary to the file
# with open("notes.json", "w") as f:
# json.dump(notes, f)
#
# # Add notes to the notebook
# note_content = tk.Text(notebook, width=40, height=10)
# note_content.insert(tk.END, content)
# notebook.forget(notebook.select())
# notebook.add(note_content, text=title)
#
# # Add a save button to the note frame
# save_button = ttk.Button(note_frame, text="Save",
command=save_note, style="TButton")
# save_button.grid(row=2, column=1, padx=10, pady=10)
#
#
# def load_notes():
# try:
# with open("notes.json", "r") as f:
# notes = json.load(f)
#
# for title, content in notes.items():
# note_content = tk.Text(notebook, width=40,
height=10)
# note_content.insert(tk.END, content)
# notebook.add(note_content, text=title)
#
# except FileNotFoundError:
# pass
#
#
# load_notes()
#
#
# def delete_note():
# current_tab = notebook.index(notebook.select())
# note_title = notebook.tab(current_tab, "text")
#
# confirm = messagebox.askyesno("Delete Note", f"Are you
sure you want to delete {note_title}?")
#
# if confirm:
# notebook.forget(current_tab)
# notes.pop(note_title)
#
# with open("notes.json", "w") as f:
# json.dump(notes, f)
#
#
# # Add style to buttons
# style.configure("TButton", font=("TkDefaultFont", 12))
#
# new_button = ttk.Button(root, text="New Note",
command=add_note, style="TButton")
# new_button.pack(side=tk.LEFT, padx=10, pady=10)
#
# delete_button = ttk.Button(root, text="Delete",
command=delete_note, style="TButton")
# delete_button.pack(side=tk.LEFT,padx=10, pady=10)
#
# style.configure("TNotebook.Tab", font=("TkDefaultFont", 14,
"bold"))
# style.configure("TNotebook", background="#ffffff")
#
# notebook.pack(padx=10, pady=10, fill=tk.BOTH,
expand=True)
#
# # Configure the root window
# root.configure(background="#ffffff")
#
# # Run the application
# root.mainloop()

elif "location" in query or "present location" in query:
import geocoder
# Use geocoder to get the current city based on IP address
g = geocoder.ip('me')
current_location = g.city
# Replace this with the code for your Jarvis to speak out the
current location
print("Your current location is " + current_location)
speak("your current location is" + current_location)
elif "instagram profile" in query or "profile on instagram " or
"insta" in query:
speak("sir please enter the name of the account you wanna
search")
name = input("Enter username correctly")
webbrowser.open(f"www.instagram.com/{name}")
time.sleep(5)
speak("my Lord do you want me to download the profile picture
of this account")
condition = takecommand().lower()
if "yes" or "yup" or "s" in condition:
mod = instaloader.Instaloader()
mod.download_profile(name, profile_pic_only=True)
speak("The profile pic you requested has been downloaded

successfully")
else:
pass
elif "take screenshot" in query or "take a snapshot" in query:
# Import necessary libraries
import pyautogui
from PIL import Image
# Capture the screen
screenshot = pyautogui.screenshot()
# Save the screenshot in the Downloads folder
screenshot_path = "C:/Users/UMAR
FARHAN/Downloads/screenshot.png"
screenshot.save(screenshot_path)
speak("Screenshot taken and saved successfully.")
