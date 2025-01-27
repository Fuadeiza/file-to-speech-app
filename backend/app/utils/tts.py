from google.cloud import texttospeech
import logging
import tempfile
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the .env file.")

# Create a logger instance
logger = logging.getLogger(__name__)

def text_to_speech(text, language_code="af-ZA"):
    """
    Generates speech using Google Cloud Text-to-Speech.

    Args:
        text: The text to convert to speech.
        language_code: The language code (e.g., "yo" for Yoruba, "ig" for Igbo, "ha" for Hausa).

    Returns:
        The path to the generated audio file.
    """
    try:
        # Log the input text and language code
        logger.debug(f"Generating speech for text: {text}")
        logger.debug(f"Language code: {language_code}")

        # Initialize the Text-to-Speech client with API key
        client = texttospeech.TextToSpeechClient(client_options={
            "api_key": GOOGLE_API_KEY
        })

        # Set the text input
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Configure the voice
        voice = texttospeech.VoiceSelectionParams(
            language_code=language_code,  # e.g., "yo" for Yoruba
            name=f"{language_code}-Standard-A"  # Choose a voice
        )

        # Configure the audio format
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16  # WAV format
        )

        # Generate speech
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )

        # Save the audio to a temporary WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(response.audio_content)
            temp_audio_path = temp_audio.name
            logger.debug(f"Audio saved to: {temp_audio_path}")
            return temp_audio_path

    except Exception as e:
        # Log any errors
        logger.error(f"Error generating speech: {str(e)}")
        raise Exception(f"Error generating speech: {str(e)}")