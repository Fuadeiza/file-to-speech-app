import React, { useState } from "react";

function FileUpload({ onSubmit, loading }) {
  const [file, setFile] = useState(null);
  const [language, setLanguage] = useState("yoruba");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleLanguageChange = (e) => {
    setLanguage(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(file, language);
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form">
      <div className="form-group">
        <label htmlFor="file">Upload File:</label>
        <input
          type="file"
          id="file"
          onChange={handleFileChange}
          accept=".pdf,.txt,.epub"
          required
        />
      </div>
      <div className="form-group">
        <label htmlFor="language">Select Language:</label>
        <select id="language" value={language} onChange={handleLanguageChange}>
          <option value="yoruba">Yoruba</option>
          <option value="igbo">Igbo</option>
          <option value="hausa">Hausa</option>
        </select>
      </div>
      <button type="submit" disabled={loading}>
        {loading ? "Processing..." : "Convert"}
      </button>
    </form>
  );
}

export default FileUpload;