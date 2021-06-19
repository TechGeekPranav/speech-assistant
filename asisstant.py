# C:\Users\User\Documents\Personal\Code and other\Python\venvspeech\speech\Scripts>activate.bat
#interpreter-C:\Users\User\Documents\Personal\Code and other\Python\venvspeech\speech\Scripts\python.exe
#Ask what can you do for commands

import speech_recognition as sr # sr as speechrec to rec
import playsound # convertin def- todo use ptech
from gtts import gTTS # google text to speech TO HELP
import random #to get random ints
from time import ctime # get time details
import webbrowser # open browser for search
import datetime # time
import time # help to get time
import os # app helper-pranav todo add app opening and make notes
from PIL import Image  # help for screenshot
import subprocess
import pyautogui #screenshot by pranav autogui
import pyttsx3
import bs4 as bs
import os
import pyjokes #give jokes

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name
# finction for writing something down
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#unused code
 #def engine_speak(text):
  #  text = str(text)
  #  engine.say(text)
   # engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:

def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1. what can you do
    if there_exists(['what can you do', 'how can you help me', 'tell me about you', 'can you tell me what you can do']):
        engine_speak('I can do many things for you')
        engine_speak('I can help you to search google, wikipedia or even youtube. I can tell you the weather, the price of something, or even the time. I can make a note for you, take a screenshot, play a game with you and make you laugh.')
    # 2. greetings
    if there_exists(['hey','hi','hello', 'hey there', 'hi alexis', 'hey alexis']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 3: name
    if there_exists(["what is your name","what's your name","tell me your name", "your name"]):
        
        if person_obj.name:
            engine_speak(f"My name is {asis_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {asis_obj.name}. what's your name?") #incase you haven't provided your name.
        
    #3. name
    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    #3. name
    if there_exists(["what is my name","what's my name","tell me my name"]):
        engine_speak("Your name must be " + person_obj.name)
    #3. name 
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 2: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    if there_exists(["joke","riddle"]):
        engine_speak(pyjokes.get_joke())

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time", 'can you tell me the time']):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search google for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on google")
    # 6. taking a note
    if there_exists(['make a note', 'write something down', 'i want to take a note', 'can you write something down']):
            engine_speak("What would you like me to write down?")
            notedown = record_audio()
            note(notedown)
            engine_speak("I've made a note of that.")

    # 7: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

     #8: price of something
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    #9. open apps
    if there_exists(['open explorer', 'open file explorer', 'open files', 'open my files', 'please open files', 'can you open files']):
        os.system('explorer')
        engine_speak("I have opened file explorer. You can now browse all your files.")

    if there_exists(['open notepad', 'open note', 'can you open notepad']):
        engine_speak("I have opened notepad!")
        os.system('notepad')

    if there_exists(['open chrome', 'open google chrome', 'can you open chrome']):
        webchrome = ("C:/Program Files/Google/Chrome/Application/chrome.exe %s")
        engine_speak("I have opened chrome for you to browse the web!")
        webbrowser.get(webchrome).open("chrome://newtab")

    if there_exists(['open edge', 'open microsoft edge', 'can you open microsoft edge']):
        webedge = ("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s")
        engine_speak("I have opened Microsoft Edge! You can browse the web!")
        webbrowser.get(webedge).open("https://google.com")

     #10. weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("This is the weather.")
     

     #11. game-stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        
        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

     #12. calc
    if there_exists(["plus","minus","multiply","divide", "power","+","-","*","/", "**"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply' or 'x':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
     #13. screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/User/Documents/Personal/Code and other/Python/venvspeech/speech/screencapturebyalexis.png')
        engine_speak('Screenshot taken!')
    
     #14 to search wikipedia for definition
    if there_exists(["i need the definition of", 'find wikipedia for', 'i need to do some research', 'can you find wikipedia for', 'can you do some research for me']):
        definition=record_audio("what do you need the definition of")
        wikisearch = 'https://en.wikipedia.org/wiki/'+definition
        webbrowser.get().open(wikisearch)
        engine_speak("This is what I found on wikipedia for"+definition)
    #2. greeting
    if there_exists(["exit", "quit", "goodbye", 'stop', 'bye', 'i have to go', 'thank you', 'go to sleep', 'shutdown']):
        engine_speak("bye")
        exit()

    #3. name
    if there_exists(["who are you", 'what are you']):
        
        engine_speak('I am alexis. your personal voice assistant')    
   
   #14. Current location as per Google maps
    if there_exists(["what is my exact location", 'where am i', 'what is my location', 'tell me where i am', 'can you tell me where i am' ]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")  
    #15. facts
    if there_exists(['longest word in the world', 'longest word in the dictionary', 'longest word', 'tell me a fact', 'fact']):
        engine_speak('The longest word in the dictionary and in the world is pneumonoultramicroscopicsilicovolcanoconiosis. It is a lung disease caused by inhaling volcano ashes.') 



time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Alexis'
person_obj.name = ""
engine = pyttsx3.init()

#config for terminal
while(1):
    voice_data = record_audio("Listening...") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond