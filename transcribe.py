import io
import uuid
import tempfile
import torch
import torchaudio
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def transcribe_audio(audio_bytes):
    """
    Transcribe audio bytes using Groq Whisper API.
    Uses torchaudio to process audio data.
    """
    print("transcribe_audio called")
    
    try:
        # Temporary file handling
        unique_prefix = f"audio_{uuid.uuid4()}_"
        # Create a temp file with .webm extension
        with tempfile.NamedTemporaryFile(prefix=unique_prefix, suffix=".webm", delete=True) as temp_audio_file:
            print(f"Saving raw bytes to {temp_audio_file.name}")
            # Write raw bytes to the file
            temp_audio_file.write(audio_bytes)
            temp_audio_file.flush() # Ensure data is written

            # Open the temporary file for reading
            with open(temp_audio_file.name, "rb") as audio_file:
                print("Sending to Groq API...")
                transcription = client.audio.transcriptions.create(
                    model="whisper-large-v3",
                    file=audio_file,
                    language='en'
                )
                print("Groq API response received")
                return transcription.text

    except Exception as e:
        print(f"Error during transcription: {e}")
        import traceback
        traceback.print_exc()
        return f"Error during transcription: {e}"



