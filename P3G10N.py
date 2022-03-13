import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import urllib.request
import urllib.parse
import re
from termcolor import colored
import pyautogui
import time 
banner="""
             _/|       |\_
            /  |       |  \\
           |    \     /    |
           |  \ /     \ /  |
           | \  |     |  / |
           | \ _\_/^\_/_ / |
           |    --\//--    |
            \_  \     /  _/
              \__  |  __/
                 \ _ /
                _/   \_   Author : Surya Dev Singh
               / _/|\_ \  Copyright : OpenSource
                /  |  \   Program Name : P3G10N 
                 / v \\
"""                                   
print(colored(banner,"green"))

def play_song(search_query):
    search_query=search_query.replace("play","")
    engine = pyttsx3.init() 
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 125)     
    volume = engine.getProperty('volume')   
    engine.setProperty('volume',5.0)    
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)  
    engine.say(f"playing {search_query}")
    print(colored(f"playing{search_query} 🎵🎵🎵 ......","green","on_grey"))
    engine.runAndWait()
    search_query=search_query.replace(" ","+")
    html=urllib.request.urlopen(f"https://youtube.com/results?search_query={search_query}")
    video_id=re.findall(r"watch\?v=(\S{11})", html.read().decode())
    wb.open(f"https://youtube.com/watch?v={video_id[0]}")
    time.sleep(7)
    pyautogui.hotkey('win', 'down')
    pyautogui.hotkey('win', 'down')

def send_message(input_query,search_query):
    # print(input_query[len(input_query)-1])
    contacts=[line.rstrip() for line in open('con.txt')]
    for i in contacts:
        if (i.split(":")[0]).lower()==input_query[1].lower():
            print("triggred")
            phone_number=i.split(":")[1]
            search_query=search_query.replace("text","")
            engine = pyttsx3.init() 
            rate = engine.getProperty('rate')   
            engine.setProperty('rate', 125)     
            volume = engine.getProperty('volume')   
            engine.setProperty('volume',5.0)    
            voices = engine.getProperty('voices')       
            engine.setProperty('voice', voices[0].id)  
            engine.say(f"texting to{search_query}")
            print(colored(f"texting to {search_query}  .....","green","on_grey"))
            engine.runAndWait()
            message_list=input_query[2:]
            message=""
            for word in message_list:
                message=message + word + " "
            message+="""
            **this is system generated message**"""
            wb.open(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
            time.sleep(12)
            pyautogui.press("enter")
            break
r = sr.Recognizer()
with sr.Microphone() as source:
    print(colored("🔈🔈speak now !!","yellow"))
    audio = r.listen(source)
search_query=r.recognize_google(audio)
input_query=search_query.split(' ')
# print(input_query)
if input_query[0]=="play":
    play_song(search_query)
if input_query[0]=="text":
    send_message(input_query,search_query)

