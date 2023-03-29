import speech_recognition as sr
import pyttsx3

recog = sr.Recognizer()

def SpeakText(command):
    out = pyttsx3.init()
    if (command != "desligar"):
        out.say(command)
    else:
        out.say("Ok Seu Lindo, Estou desligando...")
    out.runAndWait()
    
text = ""
while(text != "desligar"):
    try:
        
        with sr.Microphone() as mic:
            recog.adjust_for_ambient_noise(mic)
            print("IA: ouvindo...")
            audio = recog.listen(mic)
            text = recog.recognize_google(audio, language='pt-BR')
            text = text.lower()
            print("IA: Você disse "+text+"")
            SpeakText(text)
            
    except sr.RequestError as e:
        print("Não foi possível requisitar o pedido; {0}".format(e))
        
    except sr.UnknowValueError:
        print("Um erro desconhecido ocorreu")