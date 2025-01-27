import os
from google.cloud import translate_v3
import logging

# Create a logger instance
logger = logging.getLogger(__name__)

# Initialize Translation client
def translate_text(
    text: str,
    target_language: str,
    project_id: str = os.environ.get("GOOGLE_CLOUD_PROJECT"),
) -> str:
    """
    Translates text using the Google Cloud Translation API.

    Args:
        text: The text to translate.
        target_language: The target language code (e.g., "yo" for Yoruba, "ig" for Igbo, "ha" for Hausa).
        project_id: The Google Cloud project ID.

    Returns:
        The translated text.
    """
    try:
        # Log the input text and target language
        logger.debug(f"Translating text: {text}")
        logger.debug(f"Target language: {target_language}")

        # Initialize the Translation client
        client = translate_v3.TranslationServiceClient()

        # Define the parent resource
        parent = f"projects/{project_id}/locations/global"

        # Translate the text
        response = client.translate_text(
            contents=[text],
            target_language_code=target_language,
            parent=parent,
            mime_type="text/plain",  # Supported mime types: https://cloud.google.com/translate/docs/supported-formats
            source_language_code="en",  # Source language is English
        )

        # Extract the translated text
        translated_text = response.translations[0].translated_text

        # Log the translated text
        logger.debug(f"Translated text: {translated_text}")

        return translated_text

    except Exception as e:
        # Log any errors
        logger.error(f"Error translating text: {str(e)}")
        raise Exception(f"Error translating text: {str(e)}")