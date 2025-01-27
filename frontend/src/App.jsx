import React, { useState } from "react";
import axios from "axios";
import FileUpload from "./components/FileUpload";
import "./style.css";

function App() {
  const [downloadLink, setDownloadLink] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (file, language) => {
    if (!file) {
      setError("Please select a file.");
      return;
    }

    setLoading(true);
    setError("");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("language", language);

    try {
      const response = await axios.post("http://localhost:8000/upload/", formData, {
        responseType: "blob", // Important for downloading files
      });

      // Create a URL for the downloaded file
      const url = window.URL.createObjectURL(new Blob([response.data]));
      setDownloadLink(url);
    } catch (err) {
      setError("An error occurred. Please try again.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>File to Speech Converter</h1>
      <FileUpload onSubmit={handleSubmit} loading={loading} />
      {error && <p className="error">{error}</p>}
      {downloadLink && (
        <a href={downloadLink} download="output.wav" className="download-link">
          Download Audio
        </a>
      )}
    </div>
  );
}

export default App;