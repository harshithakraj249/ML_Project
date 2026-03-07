**AI/ML Web Application**

An AI/ML-based web application that integrates multiple machine learning functionalities including Face Recognition, Sentiment Analysis, and OCR for Indian Languages.
The application uses Vue.js for the frontend and Flask for the backend APIs.

Features
**1. Face Recognition**

Detects and identifies faces from images or videos.

Automatically tags recognized faces.

Useful for organizing and searching media files.

**2. Sentiment Analysis**

Classifies the sentiment of a given sentence.

Supported emotions include:

Happy

Sad

Neutral

Fear

Anger

Surprise

**3. OCR (Optical Character Recognition)**
Extracts text from images or PDF files.

Supports Indian languages.

Accepts formats such as:

.jpg

.png

.pdf

**Tech Stack**
**Frontend**

Vue.js

HTML5

CSS3

JavaScript

**Backend**

Flask (Python)

Machine Learning / Processing

NLP models for sentiment analysis

Face recognition libraries

OCR processing tools

Project Structure
ml_project/
│
├── backend/
│   ├── app.py
│   ├── sentiment_model/
│   ├── face_recognition/
│   └── ocr_module/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── package.json
│
└── README.md
Installation
**1. Clone the Repository**
git clone https://github.com/your-username/ml_project.git
cd ml_project
**2. Backend Setup (Flask)**

Install required Python packages:

pip install -r requirements.txt

Run the Flask server:

flask run

or

**python app.py**

The Flask backend will start on:

http://localhost:5000
**3. Frontend Setup (Vue.js)**

Navigate to the frontend folder:

cd frontend

Install dependencies:

npm install

Run the Vue development server:

npm run serve

The frontend will start on:

http://localhost:8080
Running the Application

To run the full application:

Start the Flask backend:

flask run

Start the Vue frontend:

npm run serve

Both services must be running simultaneously.

Usage

Open the application in your browser.

Navigate to My Projects.

Choose one of the available AI/ML modules:

Face Recognition

Sentiment Analysis

OCR

Upload files or enter text to process results.

Future Improvements

Real-time face detection from webcam

Improved OCR accuracy for multiple Indian languages

More NLP models for deeper sentiment analysis

User authentication and project management

Author

Developed as part of an AI/ML project integrating machine learning models with a modern web interface.# ML_Project
Sentiment Analysis, Face Recognition and OCR project with Vue js. 
