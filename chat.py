from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Microfone...")
        audio = microfone.listen(source)
        
    try:
        frase = microfone.Recongnize_google(audio, language='en')
        print("Humano..." + frase)
    except sr.UnkownValueError:
        print('bot: Isso não funcionou')
    return frase

def cria_audio(audio):
    tts = gTTS(audio, lang="en")
    tts.save('bot.mp3')
    playsound('bot.mp3')

bot = ChatBot("Chatbot")

conversa = ['Hi',
            'Hello', 
            'How are you?', 
            "I'm fine, and you?", 
            "I'm fine", 
            "That's great",
            "What's the best system?",
            'The best system is Windows']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    quest = ouvir_microfone()
    resposta = bot.get_response(quest)
    cria_audio(str(resposta))
    print('Bot: ', resposta)