# Sentiment Analysis System

## Overview
This application is a sentiment analysis system built using Streamlit. It allows users to analyze and visualize sentiment in text data from a Google Sheets document or a CSV file. The application also includes options to save analyzed data and visualize results using pie charts and histograms.

---

## Features
1. **Home Page**: Displays a welcome screen with an animation and title.
2. **Analyze Sentiment**:
   - Input text data from a Google Sheets document.
   - Perform sentiment analysis using VADER SentimentIntensityAnalyzer.
   - Save analyzed data as a CSV file.
3. **Visualize the Results**:
   - Choose between pie chart or histogram visualizations.
   - Visualize sentiment distribution or explore categorical correlations.
4. **CSV File Analysis**:
   - Load text data from a CSV file.
   - Perform sentiment analysis and save results as a CSV file.

---

## Prerequisites
### Python Libraries
Ensure you have the following Python libraries installed:
- `streamlit`
- `google-auth-oauthlib`
- `google-api-python-client`
- `vaderSentiment`
- `pandas`
- `plotly`

Install them using:
```bash
pip install streamlit google-auth-oauthlib google-api-python-client vaderSentiment pandas plotly
```

### Google Sheets API
1. Enable the **Google Sheets API** in your Google Cloud Console.
2. Download the credentials file (`key.json`) and place it in the project directory.

---

## How to Run
1. Clone the repository.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run <script-name>.py
   ```
3. Open the app in your browser (URL provided in the terminal).

---

## Application Workflow
### 1. Home Page
- Displays a welcoming image and title.

### 2. Analyze Sentiment
#### Input:
- **Google Sheet URL**: URL of the Google Sheets document.
- **Range**: Specify the range of data (e.g., `Sheet1!A1:D10`).
- **Column**: Column name containing text data.

#### Output:
- Sentiment results for each row of text (Positive, Negative, or Neutral).
- Data saved as `Review.csv`.

### 3. Visualize the Results
#### Options:
- **Pie Chart**: Displays the percentage of each sentiment.
- **Histogram**: Shows sentiment distribution across a categorical column.

### 4. CSV File
#### Input:
- **File Path**: Path to a CSV file.
- **Column**: Column name containing text data.

#### Output:
- Sentiment results for each row of text.
- Data saved as `Review.csv`.

---

## File Structure
```
|-- key.json                # Google API credentials
|-- <script-name>.py        # Streamlit application script
|-- README.md               # This file
```

---

## Known Issues
- Ensure correct Google Sheets API configuration and permissions.
- Use valid file paths and column names for CSV analysis.

---

## Future Enhancements
- Add support for more advanced NLP models.
- Integrate additional data visualization options.
- Implement user authentication for Google Sheets access.





