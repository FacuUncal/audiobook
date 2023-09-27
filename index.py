from gtts import gTTS

archivo = open('texto.txt', 'r', encoding='utf-8')
texto = archivo.read()
archivo.close()

tts = gTTS(text = texto, lang="en")
tts.save('audiobook.mp3')


