# C:\Users\User\Documents\Personal\Code and other\Python\venvspeech\speech\Scripts>activate.bat
import googlesearch
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import google
import googlesearch


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sid' in command:
                command = command.replace('sid', '')
                print(command)
    except:
        pass
    return command


def run_sid():
    command = take_command()
    print(command)
    if 'play' and 'song' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' and 'search wikipedia for' in command:
        person = command.replace('who is', '')
        search = command.replace('search wikipedia for', '')
        info = wikipedia.summary(person, 1)
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'who' and 'are' and 'you' in command:
        talk('I am Sid, your personal voice assistant.')
    elif 'help' and 'run' and 'what' in command:
        talk('the internet helps me. thank pranav who made me')
    elif 'joke' and 'jokes' in command:
        talk(pyjokes.get_joke())
    
    

    else:
        talk('Please say the command again.')


while True:
    run_sid()