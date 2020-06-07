from gtts import gTTS

from playsound import playsound

audio="sp.mp3"

language="en"

sp=gTTS(text = "hello how are you all.",
lang=language,slow=False)

sp.save(audio)
playsound(audio)
