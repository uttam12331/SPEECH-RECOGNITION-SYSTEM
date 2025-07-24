import speech_recognition as sr

def transcribe_audio_sr(audio_file_path):
    """
    Transcribes audio using SpeechRecognition library with Google Web Speech API
    """
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

transcription = transcribe_audio_sr("1.wav")
print(transcription)
