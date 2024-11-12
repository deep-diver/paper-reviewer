import os
import base64
import requests
from tqdm import tqdm
from pydub import AudioSegment  # Import pydub for audio manipulation

# You need to login to GCP using your own credentials first
# GCP_API_KEY should be set to the token obtained from `gcloud auth print-access-token`
# Your GCP project, credentials (i.e. application default, service account, etc.) should have permissions to use the Text-to-Speech API
# Ref. link: https://cloud.google.com/text-to-speech
GCP_API_KEY = os.getenv("GCP_API_KEY")

def synthesize_text(text, type="speaker1"):
    """Synthesizes speech from the input string of text."""

    if type == "speaker1":
        voice = "en-US-Journey-O"
    else:
        voice = "en-US-Journey-D"

    url = "https://texttospeech.googleapis.com/v1/text:synthesize"
    headers = {
        "Content-Type": "application/json",
        "X-Goog-User-Project": "gcp-ml-172005",  # Replace with your project ID
        "Authorization": f"Bearer {GCP_API_KEY}"
    }
    data = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": "en-US",
            "name": voice
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return base64.b64decode(response.json()['audioContent'])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def script_to_speech(conversations):
    final_audio = AudioSegment.empty()  # Initialize an empty AudioSegment

    for conversation in tqdm(conversations, desc="Generating podcast segments", unit="segment"):
        speaker1_text = conversation["Alex"]
        speaker2_text = conversation["Jamie"]

        audio1 = synthesize_text(speaker1_text, type="speaker1")
        audio1_segment = AudioSegment(audio1, sample_width=2, frame_rate=24000, channels=1)
        audio1_segment = audio1_segment.fade_in(duration=100)
        audio1_segment = audio1_segment.fade_out(duration=100)

        final_audio += audio1_segment
        if len(speaker2_text.strip()) > 0:
            audio2 = synthesize_text(speaker2_text, type="speaker2")
            audio2_segment = AudioSegment(audio2, sample_width=2, frame_rate=24000, channels=1)
            audio2_segment = audio2_segment.fade_in(duration=100)
            audio2_segment = audio2_segment.fade_out(duration=100)

            # Add a pause (e.g., 500 milliseconds = 0.5 seconds)
            pause = AudioSegment.silent(duration=200)
            final_audio += pause  # Add the pause after speaker 1
            final_audio += audio2_segment

    return final_audio