import os
import speech_recognition as sr


r = sr.Recognizer()

m = sr.Microphone()

bad_words_arr = ["hell", "fuck", "damn", "ass", "bitch"]

bad_words = {}

for w in bad_words_arr:
    bad_words[w] = True

# my_str = "Fuck you you dumb ass bitch"
#
# words_arr = my_str.lower().split(" ")


# test_arr = {
#     0: "hello",
#     1: "world",
#     2: "brandon",
#     3: "parker"
# }

print(bad_words["hell"])

while True:

    try:

        with m as source:

            audio = r.record(source, duration=3)

            text = r.recognize_google(audio)
            text = text.lower()
            words = ("{}".format(text).lower().split(" "))
            print(words)

            for w in words:
                if w in bad_words:
                    print(f"you said the bad word {w}")
                    exit()


            # if text != "":
            #     print("You're Done, You're Done")
            #     os.system('TASKKILL /F /IM RocketLeague.exe')
            #     exit()

    except sr.UnknownValueError:

        continue

    except sr.RequestError:

        continue
