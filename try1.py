from tracemalloc import stop
import pyautogui
import time
import pyttsx3
import speech_recognition as sr
import webbrowser 
import threading
import multiprocessing

global stop1
stop1=False

def print1(my):
    # print("Hello")
    time.sleep(2)
    # my="I am Kajal Singh. I study in SDSM."
    
    for i in my:
        pyautogui.keyDown(i)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

def scroll(m):
    while True:
        if stop1:
            break
        time.sleep(0.4)
        pyautogui.scroll(m)
        # speak("mode")
        # query = takeCommand().lower()
        # if 'stop' in query:
        #     speak("Stopping Scroll")
        #     break
        # elif 'down' in query:
        #     pyautogui.scroll(-300)
        # elif 'above' in query:
        #     pyautogui.scroll(300)

def type(my):
    for i in my:
        pyautogui.keyDown(i)

def speak(audio):
    engine.say(audio)
    try:
        engine.runAndWait()
    except RuntimeError:
                print("A TypeError has been occured!")
    # engine.runAndWait()


def takeCommand_scroll(ret_value):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        r.operation_timeout = 2

        audio = r.listen(source)

    try:
        print("Recognizing...")    
        ret_value.value = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
        time.sleep(1)

    except Exception as e:
        print(e)    
        speak("Say that again please...")  
        return "None" 
    return query

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        r.operation_timeout = 2

        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
        time.sleep(1)

    except Exception as e:
        print(e)    
        speak("Say that again please...")  
        return "None" 
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'out' in query:
            speak("Closing Assistant")
            break
        elif 'press' in query:
            query = query.replace("press", "")
            type(query)
        elif 'scroll' in query:
            # a=threading.Thread(target=scroll).start()
            # b=threading.Thread(target=takeCommand).start()
            # time.sleep(5)
            # try:
            #     threading.Thread(target=scroll).join()
            # except RuntimeError:
            #     print("giyo")
            # stop1=True
            # ret_value = multiprocessing.Value("d", 0.0, lock=False)
            query = query.replace("scroll", "")
            if 'down' in query:
                scroll(200)
            elif 'up' in query:
                scroll(-200)
            # print(ret_value.value)

        elif 'mouse' in query:
            query = query.replace("mouse", "")
            if 'left' in query:
                pyautogui.click()
            elif 'right' in query:
                pyautogui.click('right')
        elif 'cursor' in query:
            query = query.replace("cursor", "")
            if 'left' in query:
                pyautogui.move(-100, 0)
            elif 'right' in query:
                pyautogui.move(100, 0)
            elif 'up' in query:
                pyautogui.move(0, -100)
            elif 'down' in query:
                pyautogui.move(0, 100)
            


        elif ('search google' in query) or ('google' in query) or ('google search' in query):
            query = query.replace("google", "")
            webbrowser.get('chrome').open('google.com')
            # time.sleep(1)
            # for i in query:
            #     pyautogui.keyDown(i)
            # pyautogui.keyDown('enter')
            # time.sleep(0.5)
            # pyautogui.keyDown('enter')
            # speak("we are in google")
            # time.sleep(1)


        # while True:
    #     query = takeCommand().lower()
    #     if 'out' in query:
    #         speak("Thank You Sir")
    #         break
    #     elif 'press button' in query:
    #         query = query.replace("press button", "")
    #         press(query)
        
