# Artist-Mashup

YouTube Audio Cutter is a Flask application that allows you to download audio from YouTube, cut it into specified durations, concatenate the audio clips, and send the final audio file as a ZIP attachment via email.

## Features

- Download audio from YouTube videos
- Cut audio files into specified durations
- Concatenate audio clips into a single audio file
- Send the final audio file as a ZIP attachment via email

## Prerequisites

Before running the application, make sure you have the following installed:

- Python (version 3.7 or higher)
- Flask (install using `pip install flask`)
- youtube_dl (install using `pip install youtube_dl`)
- moviepy (install using `pip install moviepy`)
- youtubesearchpython (install using `pip install youtubesearchpython`)
- smtplib (install using `pip install secure-smtplib`)

## Usage

1. Clone this repository to your local machine.

2. Install the required Python packages by running the following command in your terminal or command prompt:


3. Open the `app.py` file and update the following placeholders:
- Replace `enter email` with the sender's email address in the `fromaddr` variable.
- Replace `enter password` with the sender's email password in the `s.login(fromaddr, "enter password")` line.

4. Run the application by executing the following command in your terminal or command prompt:


5. Open your web browser and go to `http://localhost:5000` to access the application.

6. Fill in the form fields with the desired singer name, number of videos, trim time, and your email address.

7. Click the "Submit" button to start the audio cutting process.

8. Once the process is completed, you will receive an email with the final audio file as a ZIP attachment.


