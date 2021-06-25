import os
import pandas as pd
from pydub import AudioSegment, audio_segment
from gtts import gTTS

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # 1 = generate the next train to arrive
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 3000
    finish = 5200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1.mp3", format = "mp3")

    # 2 = Platform
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 5200
    finish = 6500
    audioProcessed = audio[start:finish]
    audioProcessed.export("2.mp3", format = "mp3")

    # 3 = Train Numbber

    # 4 = Train Name
    
    # 5 = Departing from

    # 6 = To and Via Route
 
    #7 = Total coaches 
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 20000
    finish = 26000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7.mp3", format = "mp3")

    #8 = Shop Location
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 26000
    finish = 32000
    audioProcessed = audio[start:finish]
    audioProcessed.export("8.mp3", format = "mp3")

    #9 = First Class Accomodation
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 32000
    finish = 35000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9.mp3", format = "mp3")

    #10 = Unreserved seating
    audio = AudioSegment.from_mp3('announcement.mp3')
    start = 35000
    finish = 40000
    audioProcessed = audio[start:finish]
    audioProcessed.export("10.mp3", format = "mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
         # 3 = Train Numbber
         textToSpeech(item['train_no'] , '3_mp3')

          # 4 = Train Name
         textToSpeech(item['train_name'] , '4_mp3')

          # 5 = Departing from
         textToSpeech(item['from'], '5.mp3')

          # 6 = To and Via Route
         textToSpeech(item['to'] + " " + item['via'], '6.mp3')

         audios = [f"{i}.mp3" for i in range(1,10)]
         announcement = mergeAudios(audios)
         announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")





if __name__ == "__main__":
    print("Generating Skeleton....")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("trains_name.xlsx")
