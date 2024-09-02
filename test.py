import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

# # Load the audio file using the AudioFile class
# audio_file = 'harward.wav'
# with sr.AudioFile(audio_file) as source:
#     # Adjust for ambient noise (optional, can improve accuracy)
#     recognizer.adjust_for_ambient_noise(source)
    
#     # Read the entire audio file
#     audio_data = recognizer.record(source)

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Capture audio input from the microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio_data = recognizer.listen(source)


# Perform speech recognition using Google Web Speech API
try:
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print("Error: Could not request results from Google Speech Recognition service;", e)
