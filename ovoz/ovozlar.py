from gtts import gTTS
import pygame  # playsound o'rniga

# Matnni ovozga o'zgartirish
text = ("This week several senior officials in Uzbekistan have been dismissed in connection "
        "with an alleged assassination attempt on Komil Allamjonov, Uzbekistan has implemented "
        "a decree to enhance private sector participation in education, and finalized negotiations "
        "with China, accelerating its accession to the WTO.")

tts = gTTS(text, lang="en")
tts.save("output.mp3")
print("Tovush saqlandi: output.mp3")

# Ovozli faylni ijro etish
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

# Ovozli faylni matnga aylantirish
import speech_recognition as sr

recognizer = sr.Recognizer()
audio_file = "out1.wav"

try:
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("Recognized speech:", text)
except FileNotFoundError:
    print(f"Audio file '{audio_file}' topilmadi.")
except sr.UnknownValueError:
    print("Ovoz tanib olinmadi.")
except sr.RequestError as e:
    print(f"Xizmatga so'rov yuborishda xato: {e}")