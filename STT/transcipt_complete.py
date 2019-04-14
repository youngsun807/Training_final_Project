'''
- Before starting STT and executing this code
   you have to install pydub, librosa, and etc related to pydub, librosa.
- Of course, you must install Google API.
  reference site about installing Google API. https://webnautes.tistory.com/1247
  If you want to use API, write next commands on CMD(Power shell).
    1) cd location where you install API
    2) gcloud auth activate-service-account --key-file="API key location"
    3) .\'name of virtual environment'\Scripts\activate
    4) python transcribe_complete.py ---> this code
    5) deactivate ---> if you want to exit 
'''
import io
import os
import csv    
import subprocess
import shutil
import time
import datetime
import librosa
from pydub import AudioSegment

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


now = datetime.datetime.now()
# yesterday = datetime.datetime.now()-datetime.timedelta(1)
nowDatetime = now.strftime('%Y%m%d')
#자르기를 시작하는 위치, seconds
# offset = 60
offset = 0
# 자르는 크기, seconds
duration = 15

pDir = "raw sound file for splitting" # 원본파일 위치
length = librosa.get_duration(filename="raw sound file for splitting".format(nowDatetime)) # 녹음된 원본파일

# if iteration > 1:
#     iteration = 1
# int(length/duration)
iteration = 2
count = 0
for i in range(iteration):
    y, sr = librosa.load(pDir + "{}_wav.wav".format(nowDatetime), sr = 16000, mono = True, offset = offset + i*duration, duration = duration)
    
    librosa.output.write_wav("" + "file" + str(i) + ".wav", y, sr)
    count = count + 1
print("split complete!" + str(iteration) + "files made")
print(count)

for j in range(count):
    audio = AudioSegment.from_wav("storage location for splitted files" + "file" + str(j) + ".wav")

    # Google API STT service, The recognition rate is highest when it is a mono channel, .flac
    audio = audio.set_channels(1) 
    audio.export("storage location for splitted files" + str(j) + ".flac", format="flac")

time.sleep(3)
client = speech.SpeechClient()

f = open('storage location for translate text//{}_YS.csv'.format(nowDatetime), 'w', encoding='utf-8', newline='')

for i in range(count):
    with io.open("storage location for splitted files//{}.flac".format(i), 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding='FLAC',
        sample_rate_hertz=16000,
        language_code='ko_KR' # translated into Korean(South)
    )

    response = client.recognize(config, audio)

    print('Waiting for operation to complete...')

    
    for k in response.results:
        alternatives = k.alternatives
        for alternative in alternatives:
            print('translate : {}'.format(alternative.transcript))
            print('accuracy : {}'.format(alternative.confidence))

            wr = csv.writer(f)
            wr.writerow([alternative.transcript])

f.close()

