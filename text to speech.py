from gtts import gTTS

import os

b = input('enter text : ')
with open("a.txt", "w") as f:
    f.write('')
if (not os.path.exists("a.txt")):
    with open("a.txt", "w") as f:
        f.write(str(b))
with open("a.txt", "r") as f:
        mytext = f.read()

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system(" welcome.mp3")
