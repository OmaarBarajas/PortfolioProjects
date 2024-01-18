from gtts import gTTS
import os
# Providing the text
input_text = "Hola a todos mucho gusto"
# Setting the language (it can be changed)
language = "en"
# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating, saving and playing the audio file
voice.save("demo.mp3")
os.system("start demo.mp3")
