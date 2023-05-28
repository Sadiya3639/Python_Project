import pyttsx3
import webbrowser
import pywhatkit
import speech_recognition as sr
torin=pyttsx3.init("sapi5")
def voice():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as m:
            print("listening....")
            sound=r.listen(m)
            tr=r.recognize_google(sound, language="en-in")
            print("You: "+tr)
        return tr.lower()
    except:
        torin.say("Sorry LoL internet.")
        torin.runAndWait()
        return ""
comm=voice()
if "search" in comm and "youtube" in comm:
    torin.say("search for what.")
    torin.runAndWait()
    comm=voice()
    webbrowser.open(f"https://www.youtube.com/results?search_query={comm}")
if "play" in comm and "youtube" in comm:
    torin.say("Play what.")
    torin.runAndWait()
    comm=voice()
    pywhatkit.playonyt(comm)
if "youtube" in comm:
    torin.say("Ok, opening youtube.")
    torin.runAndWait()
    webbrowser.open("youtube.com")
    if "play" in comm and "shorts" in comm:
        torin.say("Play what....")
        torin.runAndWait()
        comm=voice()
        pywhatkit.playonyt(comm)
if "facebook" in comm:
    torin.say("Please wait...")
    torin.runAndWait()
    comm=voice()
    webbrowser.open("facebook.com")
    if "play" in comm and "video" in comm:
        torin.say("Please wait...")
        torin.runAndWait()
        comm=voice()
        webbrowser.open("https://www.facebook.com/watch/?ref=tab")
        if "play" in comm and "reels" in comm:
            torin.say("Please wait...")
            torin.runAndWait()
            comm=voice()
            webbrowser.open("https://www.facebook.com/reel")
            if "play" in comm and "reels" in comm:
                torin.say("Please wait...")
                torin.runAndWait()
                comm=voice()
                webbrowser.open("https://www.facebook.com/watch/shows")
                if "play" in comm and "reels" in comm:
                    torin.say("Please wait...")
                    torin.runAndWait()
                    comm=voice()
                    webbrowser.open("https://www.facebook.com/watch/live/?ref=watch")
if "facebook" in comm and "messages" in comm:
        torin.say("Please wait...")
        torin.runAndWait()
        comm=voice()
        webbrowser.open("https://www.facebook.com/messages/t/")
if "facebook" in comm and "profile" in comm:
    torin.say("Please wait...")
    torin.runAndWait()
    comm=voice()
    webbrowser.open(f"https://www.facebook.com/profile.php?id={comm}")
if "search" in comm and "google" in comm:
    torin.say("search for what.")
    torin.runAndWait()
    comm=voice()
    webbrowser.open(f"https://www.chrome.com/search?q={comm}")
if "instagram" in comm:
    torin.say("Please wait...")
    torin.runAndWait()
    comm=voice()
    webbrowser.open("instagram.com")
    if "instagram" in comm:
        torin.say("Please wait...")
        torin.runAndWait()
        comm=voice()
        webbrowser.open("https://www.instagram.com/?utm_source=")
        if "instagram" in comm and "explore" in comm:
            torin.say("Please wait...")
            torin.runAndWait()
            comm=voice()
            webbrowser.open("https://www.instagram.com/explore/")
            if "instagram" in comm and "reels" in comm:
                torin.say("Please wait...")
                torin.runAndWait()
                comm=voice()
                webbrowser.open("https://www.instagram.com/reels/")
                if "instagram" in comm and "messages" in comm:
                    torin.say("Please wait...")
                    torin.runAndWait()
                    comm=voice()
                    webbrowser.open("https://www.instagram.com/direct/inbox/")
                    if "instagram" in comm and "profile" in comm:
                        torin.say("Please wait...")
                        torin.runAndWait()
                        comm=voice()
                        webbrowser.open(f"https://www.instagram.com/={comm}")

            




