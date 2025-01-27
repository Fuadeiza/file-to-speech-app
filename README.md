# Text-to-Speech (TTS) API

This is a FastAPI-based application that allows users to upload a file, extract text from it, translate the text (if needed), and convert it into speech. The generated audio file is then returned for download.

## Features

- **File Upload**: Accepts various file formats (e.g., PDF, DOCX, TXT) for text extraction.
- **Text Extraction**: Extracts text from the uploaded file.
- **Translation**: Translates the extracted text into a specified language.
- **Text-to-Speech**: Converts the translated text into an audio file.
- **Audio Download**: Returns the generated audio file for download.

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.10 or higher
- A Google Cloud API key for translation and text-to-speech services
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Fuadeiza/tts-api.git
   cd tts-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Google Cloud API key to the `.env` file:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoint

### Upload File and Generate Audio

- **URL**: `/upload/`
- **Method**: `POST`
- **Parameters**:
  - `file`: The file to upload (required).
  - `language`: The target language for translation and TTS (default: `af-ZA`).
- **Response**: Returns the generated audio file for download.

#### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/upload/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@example.pdf" \
     -F "language=es-ES"
```

#### Example Response

The response will be an audio file (`output.wav`) that you can download and play.

## Logging

The application logs all activities and errors to `app.log` and the console. Logs include:

- Extracted text
- Translation details
- Errors during processing

## Error Handling

If an error occurs during file processing, the API will return a `500 Internal Server Error` with a detailed error message.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
- [Google Cloud Translation](https://cloud.google.com/translate) for text translation.
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech) for converting text to speech.

---

Feel free to customize this README to better fit your project's needs!# file-to-speech-app
