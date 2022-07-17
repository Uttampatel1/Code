import os
import pywhatkit as pw
import datetime
import speech_recognition as sr
import pyaudio
import pyttsx3
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "dog" in command:
                command = command.replace('dog','')
                print(command)
                #return command
                
    except:
        pass
    return command

def run_jarvis():
    
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing...'+song)
        print(song)
        pw.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('corrent time is '+time)


    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke =pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "i love you" in command:
        talk("love you too sir..")

    elif 'hi' in command:
        talk(f"hii {os.getlogin()} nice to meet you ")

    elif 'who are you' in command:
        talk("i am a artificial intelligence robot")

    elif "date me" in command:
        talk("sorry, i am a robot.")

    elif "khushi" in command:
        talk("hii how are you khushi")
        print("dfjgdskrgnjdrsk")

    else:
        pw.search(command)   

#run_jarvis()


i=0
while i<3:
    run_jarvis()
    i+=1

