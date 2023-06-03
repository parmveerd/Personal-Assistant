import speech_recognition as sr
import os
import keyboard
import subprocess
import openai
import pyttsx3
import pyautogui
import psutil
import time
import shutil
from pytube import YouTube
# from download import title

# storing previous chatgpt conversations
conversation = []

timer = False

# initialize
r = sr.Recognizer()

# speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# voice type
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# speak helper function
def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    while True:
        try:
            print("Read for command")
            
            # keyboard combo to start listening
            keyboard.wait("ctrl+alt+s")
            
            print("Listening...")

            # Listen for 5 seconds
            audio_data = r.listen(source, phrase_time_limit = 3)
            print("Recognizing...")

            text = r.recognize_google(audio_data)
            print(f"you said: {text}")
            
            if "open edge" in text.lower():
                subprocess.Popen(r"location")
                print("Opened edge!")
                speak("Opened edge.")
            
            elif "open firefox" in text.lower():
                subprocess.Popen(r"location")
                print("Opened firefox!")
                speak("Opened firefox.")

            elif "open mail" in text.lower():
                # open without using the file path
                pyautogui.press('win')
                time.sleep(1)
                pyautogui.write('mail')
                time.sleep(1)
                pyautogui.press('enter')
                print("Here is your mail.")
                speak("Here is your mail.")

            elif "play music" in text.lower():
                # subprocess.Popen(r"C:\Program Files\WindowsApps\AppleInc.iTunes_12128.2.57059.0_x64__nzyj5cx40ttqa\iTunes.exe")
                # print("done")
                speak("Staring music")
                exec(open(r"location").read())

            elif "pause music" in text.lower():
                if "iTunes.exe" in (i.name() for i in psutil.process_iter()):
                    # subprocess.Popen(r"C:\Program Files\WindowsApps\AppleInc.iTunes_12128.2.57059.0_x64__nzyj5cx40ttqa\iTunes.exe")
                    # time.sleep(5)
                    # pyautogui.press('space')

                    # or can do it this way
                    exec(open(r"location").read())
                else:
                    print("There is no music playing to pause.")
                    speak("There is no music playing to pause.")

            elif "search google for" in text.lower():
                # select the second element after splitting and search it in google
                temp = text.lower().split("search google for ")[1]
                temp = temp.replace(" ", "+")
                os.system(f"start https://www.google.com/search?q={temp}")

            elif "download music" in text.lower():
                speak("Please enter the link.")
                # enter video url
                link = str(input("Please enter the link: "))
                # call the download python file
                exec(open(r"location").read())
                print("The song has been downloaded.")
                speak("The song has been downloaded.")

            elif "move file to music" in text.lower():
                # where file is downloaded into:
                src = r"location"
                # the file path for iTunes downloaded music:
                dest = r"location"
                # move the files:
                shutil.move(src, dest)
                print("The song has been moved to iTunes.")
                speak("The song has been moved to iTunes.")
                     
            elif "gpt " in text.lower():
                openai.api_key = "key"
                
                model = "davinci"
                temp = text.lower().split("gpt ")[1]
                t = 0.7
                max_chars = 256

                response = openai.Completion.create(
                    model = "text-davinci-003", 
                    prompt = temp, 
                    t = t, 
                    max_chars = max_chars
                )

                print(response.choices[0].text.strip())
                speak(response.choices[0].text.strip())
            
            elif "chat gpt" in text.lower():
                openai.api_key = ""
                temp = text.lower().split("chat gpt ")[1]
                conversation.append({"role":"user", "content":temp})
                response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo", 
                    messages = conversation
                )
                chatgpt = response['choices'][0]['message']['content']
                print(chatgpt)
                speak(chatgpt)
            
            elif "start timer" in text.lower():
                timer = True
                start_time = time.time()
                print("Started timer.")
                speak("Started timer.")
            
            elif "stop the stopwatch" in text.lower():
                if timer:
                    end_time = time.time()
                    total = end_time - start_time
                    total = "{:.3f}".format(total)
                    print(f"The timer was on for {total} seconds.")
                    speak(f"The timer was on for {total} seconds.")
                    timer = False
                else:
                    print("The timer was never started.")
                    speak("The timer was never started.")

            elif "what time is it" in text.lower():
                o = time.localtime()
                t = time.asctime(o)
                print(f"It is {t}")
                speak(f"It is {t}")

            elif "take a picture" in text.lower():
                p = subprocess.Popen(r"location")
                print("Taking a picture in 3 seconds.")
                speak("Taking a picture in three seconds.")
                time.sleep(3)
                pyautogui.press('enter')
                print("Picture taken.")
                speak("Picture taken.")
                time.sleep(2)
                p.kill()

            elif "what is the weather" in text.lower():
                subprocess.Popen(r"location")
                print("Here is the weather.")
                speak("Here is the weather.")

            elif "open notes" in text.lower():
                subprocess.Popen(r"location")
                print("Here are your notes.")
                speak("Here are your notes.")

            elif "open school website" in text.lower():
                os.system("start link")
                print("Opening website.")
                speak("Opening website.")

            elif "shutdown computer now" in text.lower():
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")



        except:
            print("Something went wrong... Please try again.")
            speak("Something went wrong... Please try again.")
