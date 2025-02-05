import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit
import pyautogui
import playsound
import pyaudio
import wave
import requests
import googletrans
import wolframalpha
from googletrans import Translator
import webbrowser
import time

wolfram_api = "6WUHYR-68XTAVJ9HE"
news_api_key = "4453c1f2f32d4fa7ba7b47a0fbbad1cc"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
translator = Translator()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("wait for few minutes....")
        query = r.recognize_google(audio, language="en")
        print(f"You said : {query}\n")
    except Exception as e:
        print(e)
        print("Sorry could not get that! Try again..")
        query = "none"
    return query


def wakeUpCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant is Offline...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=3)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en")
        print(f"You said:{query}\n")
    except Exception as e:
        query = "none"
    return query


# Capital of the Country
def wolfarm_alpha_country_capital(query):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(query)
    answer = next(result.results).text
    answer_split = answer.split()
    capital_result = "The capital of " + answer_split[-1] + " is " + answer_split[0]
    print(capital_result)
    speak(capital_result)


# Calculator
def wolfram_alpha_calculator(query):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(query)
    answer = next(result.results).text
    print(answer)
    speak("The answer is " + answer)


# President of a certain country
def wolfram_alpha_president(query):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(query)
    answer = next(result.results).text
    print(answer)
    speak("The president is " + answer)


# Prime Minister of a certain country
def wolfram_alpha_primeminister(query):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(query)
    answer = next(result.results).text
    print(answer)
    speak("The prime mister is " + answer)


def wolfram_alpha_query(query):
    try:
        client = wolframalpha.Client(wolfram_api)
        result = client.query(query)
        answer = next(result.results).text
        print(answer)
        speak(answer)
    except Exception as e:
        print("Sorry, I couldn't process your query: ", e)
        speak("Sorry, I couldn't process your query.")


def get_news():
    news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + news_api_key
    try:
        news = requests.get(news_url).json()
        articles = news["articles"]

        news_headlines = []
        for article in articles:
            news_headlines.append(article["title"])

        for i in range(3):
            print(news_headlines[i])
            speak(news_headlines[i])
    except Exception as e:
        print("Error fetching news:", e)
        speak("sorry, I couldn't retrieve the latest news.")


def wishme():
    try:
        day = datetime.datetime.now()
        hour = day.hour
        if hour >= 0 and hour < 12:
            print("Good Morning!...")
            speak("Good Morning!...")
        elif hour == 12:
            print("Good Noon!...")
            speak("Good noon!...")
        elif hour > 12 and hour < 5:
            print("Good Afternoon!...")
            speak("Good Afternoon!...")
        else:
            print("Good Evening!...")
            speak("Good Evening!...")
    except Exception as e:
        print("Greetig error:", e)
        speak("Sorry, I couldn't greet you properly. ")


def write_text_in_notepad():
    print("Please tell me what should i write")
    speak("Please tell me what should i write")
    text = commands()
    os.startfile("notepad.exe")
    pyautogui.typewrite(text, interval=0.25)


def translate_text():
    try:
        speak("Please tell me the text you want to translate")
        text = commands()
        print("Text to translate:", text)
        speak("Please tell me the language you want to translate to")
        language = commands()
        print("Target language:", language)
        translated = translator.translate(text, dest=language)
        speak(f"Translated text is {translated.text}")
    except Exception as e:
        print("Error in translation: ", e)
        speak("Sorry,there was an error during translation.")


def record_audio(filename="recorded_audio.wav", duration=10):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    p = pyaudio.PyAudio()
    stream = p.open(
        format=sample_format,
        channels=channels,
        rate=fs,
        frames_per_buffer=chunk,
        input=True,
    )

    print("Recording...")
    frames = []

    start_time = time.time()
    while time.time() - start_time < duration:
        data = stream.read(chunk)
        frames.append(data)

    speak("Recording finished...")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b"".join(frames))
    wf.close()


# Play Audio
def play_audio(filename="recorded_audio.wav"):
    try:
        with playsound.playsound(filename) as sound:
            sound.play()
    except Exception as e:
        print("Error playing audio: {}".format(e))
        # you may want to add some code here to handle the exception


# Function to open Instagram
def open_instagram():
    webbrowser.open("https://www.instagram.com")


# Function to open Facebook
def open_facebook():
    webbrowser.open("https://www.facebook.com")


# Function to open Twitter
def open_twitter():
    webbrowser.open("https://www.twitter.com")


# Function to open WhatsApp
def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")


# Function to open YouTube
def open_youtube():
    webbrowser.open("https://www.youtube.com")


if __name__ == "__main__":
    # wishme()
    while True:
        query = wakeUpCommands().lower()
        if "hello" in query or "hey" in query or "hi" in query or "wake up" in query:
            print("Activating Assistant...")
            speak("Activating Assistant...")
            print("Going Online...")
            speak("Going Online...")
            wishme()
            print("I am here to support you. Can you please tell me your name?")
            speak("I am here to support you. Can you please tell me your name?")
            listen_name = commands()
            print("Hi " + listen_name + " nice to meet you")
            speak("Hi " + listen_name + " nice to meet you")
            print("what can i do for you!")
            speak("what can i do for you!")
            while True:
                query = commands().lower()
                if "hello" in query:
                    print("Hello, how are you")
                    speak("Hello, how are you")
                elif "i'm Fine" in query or "good" in query:
                    print("Great to hear that you're feeling good")
                    speak("Great to hear that you're feeling good")
                elif " how are you " in query or "what about you" in query:
                    print("Perfect Sir, I’m doing well.")
                    speak("Perfect Sir, I'm  doing well.")
                elif "tell me about yourself" in query:
                    print(
                        "I'm your persional virtual assistant, I'm here to support you and work for you. I don't need a break and i will never ask for day off"
                    )
                    speak(
                        "I'm your persional virtual assistant, I'm here to support you and work for you. I don't need a break and i will never ask for day off"
                    )
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"The Current time is {strTime}")
                    speak(f"The Current time is {strTime}")
                elif "open google" in query:
                    print("Opening Google Application...")
                    speak("Opening Google Application...")
                    os.startfile(
                        "C:\\Program Files\Google\Chrome\Application\chrome.exe"
                    )
                elif "play" in query and "song" in query:
                    query = query.replace("play", "")
                    speak("Playing " + query)
                    pywhatkit.playonyt(query)
                elif "stop" in query:
                    pyautogui.press("K")
                    speak("Video  Stopped")
                elif "play" in query:
                    pyautogui.press("K")
                    speak("Video  play")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("Unmuted")
                # wolfram Alpha - capital of country
                elif "capital" in query and "of" in query:
                    wolfarm_alpha_country_capital(query)

                # wolfram Alpha - calculator
                elif "solve" in query or "calculation" in query or "compute" in query:
                    speak("Sure, can you give me an input to perform the calculation?")
                elif (
                    "+" in query
                    or "-" in query
                    or "multiply" in query
                    or "divide" in query
                    or "root" in query
                ):
                    wolfram_alpha_calculator(query)

                # wolfram Alpha - President
                elif "who" in query and "president" in query:
                    wolfram_alpha_president(query)

                # wolfram Alpha - Prime Minister
                elif "who" in query and "prime minister" in query:
                    wolfram_alpha_primeminister(query)

                elif "weather" in query or "temperature" in query or "formula" in query:
                    wolfram_alpha_query(query)
                elif (
                    "who is" in query
                    or "what " in query
                    or "where " in query
                    or "when " in query
                    or "why " in query
                    or "how " in query
                ):
                    wolfram_alpha_query(query)

                # Top 3 News - Headlines
                elif "news" in query:
                    speak("Allright, let me tell you the first three headlines")
                    get_news()

                elif "write" in query and "notepad" in query:
                    write_text_in_notepad()
                    if "stop writing" in query:
                        speak("Stopping Writing")
                        quit()
                elif "record voice" in query:
                    speak("audio is recorded")
                    record_audio()
                elif "play recording" in query:
                    play_audio()
                elif "translate" in query:
                    translate_text()
                elif "open instagram" in query:
                    speak("Opening Instagram")
                    open_instagram()
                elif "open facebook" in query:
                    speak("Opening Facebook")
                    open_facebook()
                elif "open twitter" in query:
                    speak("Opening Twitter")
                    open_twitter()
                elif "open whatsapp" in query:
                    speak("Opening Whatsapp")
                    open_whatsapp()
                elif "open youtube" in query:
                    speak("Opening YouTube")
                    open_youtube()
                elif "close" in query:
                    pyautogui.press("ctrl+w")
                    speak("tab close")

                elif (
                    " search in google" in query or "find" in query or "google" in query
                ):
                    query = query.replace("google", "").strip()
                    search_url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(search_url)
                elif "mute" in query:
                    speak("I'm muting,Going Offline. See You Soon.")
                    break
                elif "stop" in query:
                    speak("It was a pleasure to help you, I wish you a wonderful day")
                    speak("I'm Leaving, BYE!")
                    quit()
