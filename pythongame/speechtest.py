import time

import speech_recognition as sr
# import psutil,os
import subprocess

r = sr.Recognizer()
# r.pause_threshold = .5
# r.energy_threshold = 1500

steam = subprocess.Popen(['C:\Program Files (x86)\Steam\steam.exe'])

m = sr.Microphone()

while True:
    print("while")
    try:

        with m as source:
            # r.adjust_for_ambient_noise(mic, duration=0)

            audio = r.record(source, duration=3)
            # audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            words_list = []
            words = ("{}".format(text))
            print(words)
            words_list.append(text)

            if "f***" in words or "s***" in words or "c***" in words or "cock" in words\
                    or "dammit" in words or "damn" in words or "jesus christ" in words:
                print("Naughty Boy")
                steam.kill()
                exit()


    except sr.UnknownValueError:
        # recognizer = sr.Recognizer()
        print("Unknow Value Error")
        continue

    except sr.RequestError:
        print("Oops")
        continue


