from gtts import gTTS
import os
# Providing the text file
f = open("text.txt", "r")
# reading the file
input_text = f.read().replace("\n", " ")
# Setting the language (it can be changed)
language = "es"
# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)
# Creating, saving and playing the audio file
voice.save("txt.mp3")
os.system("start txt.mp3")
