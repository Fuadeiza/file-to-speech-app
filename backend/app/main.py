from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from app.utils.file_parser import extract_text_from_file
from app.utils.translator import translate_text
from app.utils.tts import text_to_speech
import tempfile
import logging

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), language: str = "af-ZA"):
    try:
        # Extract text from the file
        text = extract_text_from_file(file)

        # Log the extracted text
        logger.debug(f"Extracted text: {text}")

        # Translate text to the selected language (if needed)
        translated_text = translate_text(text, language)

        # Generate speech
        audio_output_path = text_to_speech(translated_text, language)

        # Return the audio file for download
        return FileResponse(audio_output_path, media_type="audio/wav", filename="output.wav")

    except Exception as e:
        # Log any errors
        logger.error(f"Error processing file: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))