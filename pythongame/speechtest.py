import os
import pygame
import speech_recognition as sr

pygame.init()

scraysound = pygame.mixer.Sound('granny_bed_jumpscare_sound_effectmp3converter.mp3')

bad_words_arr = ["hell", "fuck", "damn", "ass", "bitch", "shit", "whore", "god", "jesus christ", "holyshit", "retarded", "faggot", "niger",
                 "cont"]


bad_words = {}

for w in bad_words_arr:
    bad_words[w] = True


r = sr.Recognizer()
# r.pause_threshold = .5
# r.energy_threshold = 1500

m = sr.Microphone()

while True:

    try:

        with m as source:

            audio = r.record(source, duration=1.5)
            text = r.recognize_google(audio)
            words = ("{}".format(text).lower().split(" "))
            print(text)
            for w in words:
                if w in bad_words or "*" in w:
                    scraysound.play()
                    continue






            # print("You're Done, You're Done")
                    # os.system('TASKKILL /F /IM RocketLeague.exe')
                    # exit()



    except sr.UnknownValueError:
        # recognizer = sr.Recognizer()
        continue

    except sr.RequestError:

        continue


