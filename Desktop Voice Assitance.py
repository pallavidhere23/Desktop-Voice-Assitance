import webbrowser     # Access Web portal through our code
import pyttsx3 		 # Facilitate text to speech module
import speech_recognition as sr  # It is a speach recognition module as part of google Speech Api
import wikipedia	# Browse or surf anything on Wikipedia
import datetime		# Access System datetime
import os			# Lauch or Open System Folders and application
import random		# generate random numbers
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[0].id)  
engine.setProperty('voice',voices[0].id)     #set the audio of voice assistant as david
rate = engine.getProperty('rate')				# Go to Start Search for Microphone Setup
newrate = 130								# You will find  David as default voice
engine.setProperty('rate', newrate)			# We have encapsulated Hari with David's Voice
def speak(audio):
    engine.say(audio)						# Here is a function  to intake audio
    engine.runAndWait()
def wishMe():
    speak("Hello miss pallavi. Welcome")
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")					# This Function  is to greet the  Owner  as per System Time
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!!")				# We can dyanamically modify as per requirements
    elif hour>=18 and hour<22:
        speak("Good Evening !")
    else:
        speak("Ma'am!! It's beyond 10pm We must Sleep")
    speak("I am Har e .  How may I help You ")
def takeCommand():
    #It takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.non_speaking_duration = 0.6			# Actual Setup for Microphone based input
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User Said: "+r.recognize_google(audio))
        i = random.randrange(0,50)
        if i<25:								# Accepting voice and recognizing
            speak("Copy that")
        else:
            speak("Roger that")
    
    except Exception as e:
        #print(e)
        print("Ma'am I was unable to hear you Please Say again")   # if there occurs some exception It will ask to 
        speak("Ma'am I was unable to hear you Please Say again")		#Speak Again
        return "None"
        
    return query    
        
       
if __name__ == "__main__":
    
    wishMe()  # function has been called to greet the owner
	   
    while True:    # Infinite  Loop  
        query = takeCommand().lower()    # Converting Voice commands to lower in order to 
        # logic for execution tasks based on query		# Relax for comparision
        if 'ok bro' or 'bro' in query:   			# Activation point
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')  		# Surf to Wikipedia
                query = query.replace("wikipedia", "")   
            #print(query)
                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia")    
                print(results)
                speak(results)          
            elif 'open youtube' in query: 
                speak("Opening YouTube For You.")
                webbrowser.open("https://www.youtube.com/")
            elif 'google' in query:            					# Browse to google Services
                if 'maps' in query:
                    speak("Opening Google Maps For you.")
                    webbrowser.open("https://www.google.co.in/maps/")
                elif 'drive' in query:
                    speak("Opening Google Drive for you.")
                    webbrowser.open("https://drive.google.com/drive/")
                elif 'translate' in query:
                    speak("Opening Google translate for you.")
                    webbrowser.open("https://translate.google.co.in/")
                else:
                    speak("Opening Google for you.")
                    webbrowser.open("https://www.google.co.in/") 
            elif 'i am sad' in query:
                webbrowser.open("https://music.amazon.in/?refMarker=dm_wcp_af_r&ref_=dm_lnd_pm_listn_f85b5c0b_sv_dmusic_0&")
                speak("Playing Music for You as refreshment")
            elif 'udemy' in query:
                speak("Opening Udemy for You")
                webbrowser.open("https://www.udemy.com/")
            elif 'pluralsight' in query:
                speak("Opening PluralSight for You.")
                webbrowser.open("https://www.pluralsight.com/")				# Access frequently used web portals
            elif 'coursera' in query:
                speak("Opening Coursera for You.")
                webbrowser.open("https://www.coursera.org/")
            elif 'thank you' in query:
                speak("You are Most Welcome It's my Honor.")            # Thank You          	   
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is  {strTime}")
            elif 'open dev c' in query:								#  Open System Applications
                codePath = "C:\Program Files (x86)\Dev-Cpp"
                os.startfile(codePath)
            elif 'microsoft teams' in query:
                path = r"C:\Users\Pallavi Dhere\AppData\Local\Microsoft\Teams"  #  Another Example
                os.startfile(path)
            elif 'exit' in query:
                print("Quiting")
                speak("Bye Bye Sir. Hope to see you Soon.")				# Come put of the code
                break
