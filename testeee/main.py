import requests
import json
from audio_handler.convert import *
from audio_handler.search import *
from session.session_handler import *   



def recognizer(session_id:str, data:str, model_id="FarFieldRus10:offline", url="https://cloud.speechpro.com/vkasr/rest/v2/recognizer/simple"):
    header = {"X-Session-Id":session_id}
    data = {
    "model_id": model_id,
    "audio": {
        "data": data,
        "mime": "WAV"
        },
    "recognition_config": {
        "additional_words": [],
        "vocabulary_ids": []
        }
    }

    print("послал [PUT] на [v2/recognizer/simple]")

    response = requests.put(url=url,headers=header,json=data)
    text = response.json()
    print(f"{response}\n{text}")



def main():
    mp3_files = search_mp3("/home/defo/Documents/testeee/files")         #Поиск файлов
    WAV_files = []
    for path in mp3_files:                                               #Конверт файлов в WAV
        WAV_files.append(mp3_to_wav(path=path))
    
    session_id = start_session()  #start session

    for wav_path in WAV_files:                                           #Перебор WAV
        data = wav_to_base64(wav_path)                                      #WAV to BASE64
        recognizer(session_id,data)                                         #BASE 64 в PUT/v2/recognizer

    stop_session(session_id)                                             #Стоп
        
        
    
    
    # data = wav_to_base64(wav_path)
    # recognizer(session_id,data)
    

if __name__ == "__main__":
    main()
