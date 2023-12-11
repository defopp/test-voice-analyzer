import time
import requests
from api.session_handler import *  
from data_handler.convert import *
from data_handler.search import *


# def recognizerCRT(file_name:str, session_id:str, data:str, model_id:str="FarFieldRus10:offline", url:str="https://cloud.speechpro.com/vkasr/rest/v2/recognizer/simple") -> str: 
    
#     header = {"X-Session-Id":session_id}
#     data = {
#     "model_id": model_id,
#     "audio": {
#         "data": data,
#         "mime": "WAV"
#         },
#     "recognition_config": {
#         "additional_words": [],
#         "vocabulary_ids": []
#         }
#     }

#     print("послал [PUT] на [v2/recognizer/simple]")
#     response = requests.put(url=url,headers=header,json=data)
#     text = response.json()["text"]

#     print(f"\n\n\n[ЦРТоблако][{file_name}]Output:")                                             
#     print(f"{file_name}:{text}")
#     return text


def recognizerCRT(mp3file:str, session_id:str, model_id:str="FarFieldRus10:offline", url:str="https://cloud.speechpro.com/vkasr/rest/v2/recognizer/simple") -> str: 
    file_name = file_name = mp3file.split("/")[-1][:-4]
    wavfile = mp3_to_wav(mp3file)
    data = wav_to_base64(wavfile)
    start = time.monotonic()

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
    print("[ЦРТоблако]Отправка...")
    response = requests.put(url=url,headers=header,json=data)
    text = response.json()["text"]
    print("[ЦРТоблако]Ответ получен...")

    end = time.monotonic()-start 
    print(f"[ЦРТоблако][{file_name}] вывод: длина текса = {len(text.split())} слов / {round(end,1)}с")                                             
    #print(f"{file_name}:{text}\n")
    return file_name, text


