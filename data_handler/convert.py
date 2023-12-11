from pydub import AudioSegment
import base64
import os


def mp3_to_wav(path: str):
    filename = os.path.basename(path)[0:-4:] #название файла без .формата.
                                    
    output_path = f'temp/{filename}.wav'    #путь вывода

    output_directory = os.path.dirname(output_path)
    os.makedirs(output_directory, exist_ok=True)  #создание файла в /files/temp

    sound = AudioSegment.from_mp3(path)     #load mp3
    sound.export(output_path, format="wav") #export mp3
    
    print(f"[OK]mp3->wav")
    return output_path



def wav_to_base64(path: str): #берет wav файл и возвращает BASE64 строку
    enc = base64.b64encode(open(path, "rb").read()) #wav to base64 
    enc = str(enc, 'ascii', 'ignore')                #ascii
    
    print("[OK]wav->base64")
    return enc