import gtts   #google text to speech 
import playsound
text = input("Enter something here: ")
sound = gtts.gTTS( text, lang = "en" )
sound.save("Welcome.mp3")
playsound.playsound ("Welcome.mp3")