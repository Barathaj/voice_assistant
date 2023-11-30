import speech_recognition as sr
import pyttsx3

listener=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("I am your alexa")

engine.say('what can i do for you')

engine.runAndWait()


def talk(comm):
    engine.say(comm)
    engine.runAndWait()

def mic():
    try:
        with sr.Microphone() as source:
            print("listining...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()

            if 'alexa' in command:
                talk(command)




    except:
        pass

def main():
    print("hi")
    engine.say('say the question clearly')
    mic()

main()





