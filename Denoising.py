import requests
import base64
from pydub import AudioSegment

url = "https://proxy.api.deepaffects.com/audio/generic/api/v2/async/denoise"

querystring = {"apikey":"w2kCXFyGpxitDQC3v48sr5E33skriti9", "webhook":"https://webhook.site/258ac3dd-67ed-4a9f-9d49-1cc1bab26d4d"}

payload = {
    "encoding": "Wave",
    "languageCode": "en-US",
    "sampleRate": 8000
}

# The api accepts data either as a url or as base64 encoded content
# passing payload as url:
payload["url"] = "output/denoised1.wav"
# alternatively, passing payload as content:
with open('output/denoised1.wav', 'rb') as fin:
    audio_content = fin.read()
payload["content"] = base64.b64encode(audio_content).decode('utf-8')

headers = {
    'Content-Type': "application/json",
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.text)

# print(response.response.url)