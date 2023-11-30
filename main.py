from data_handler.convert import *
from data_handler.search import *
from data_handler.analyzer import *
from api.session_handler import *   
from crt import *
from alphacer import*


phrase_to_search = ["мрт","врач","ренген","рэп","здравствуйте","нет","да","прием"]
#phrase_to_search = ["мрт","нет","да","прием"]

type_of_search = int(input("[1] - Подсчет листа слов(вместе) //слово1,слово2,слово3 - количество упоминаний \n[2] - Подсчет листа слов(отдельно) //слов1 - количество раз //слов2 - количество раз //слов3 - количество раз\nВыберите тип распознавания: "))

mp3_files = search_mp3("/home/defo/Documents/testeee/files")    



def crtCycle(mp3_files:list) -> dict:                                                                                  
    
    session_id = start_session()  

    finalAnalyze = {}  
    for mp3_file in mp3_files:                                  
        filename, text = recognizerCRT(mp3file=mp3_file, session_id=session_id)                                         
         
        print(f"Цикл рекогнайза {filename} завершен")
        fileAnalyze = search_words(opt=type_of_search, words=phrase_to_search, text=text)
        finalAnalyze = (dictSum(finalAnalyze,fileAnalyze)) 
     
    print("__"*60+f"\n[Вывод crtCycle]: \n{finalAnalyze}\n"+"__"*60)
    stop_session(session_id)                                             
    return fileAnalyze   







###################### оптимизировать #######################################################

# async def alphacerCycle() -> dict: ###########################################################################################################
#     mp3_files = search_mp3("/home/defo/Documents/testeee/files")        #Поиск файлов
    
#     WAV_files = []
#     for path in mp3_files:                                               #Конверт файлов в WAV
#         WAV_files.append(mp3_to_wav(path=path))
    
    
#     finalAnalyze = {}
#     for wav_path in WAV_files:################################################################Перебор WAV в РЕКОГНАЙЗ
#         file_name = wav_path.split("/")[-1][:-4]
#         text = await recognizerALPHACER(mp3filePATH=wav_path)

#         fileAnalyze = search_words(opt=type_of_search,words=phrase_to_search, text=text)
#         finalAnalyze.update(dictSum(finalAnalyze,fileAnalyze))

#     print(f"Вывод alphacerCycle [всего]: {finalAnalyze}")
#     print("[Цикл рекогнайза Alphacer завершен]\n\n\n")
#     return fileAnalyze

# async def TalphacerCycle() -> dict: ###########################################################################################################
#     mp3_files = search_mp3("/home/defo/Documents/testeee/files")        #Поиск файлов
    
#     finalAnalyze = {}
#     for mp3_path in mp3_files:################################################################Перебор mp3 в РЕКОГНАЙЗ
#         #file_name = mp3_path.split("/")[-1][:-4]
#         text = await recognizerALPHACER(mp3filePATH=mp3_path)

#         fileAnalyze = search_words(opt=type_of_search,words=phrase_to_search, text=text)
#         finalAnalyze.update(dictSum(finalAnalyze,fileAnalyze))

#     print(f"\nвывод alphacerCycle [всего]: {finalAnalyze}\n\n")
#     return fileAnalyze






if __name__ == "__main__":
    crtCycle(mp3_files)
    #asyncio.run(alphacerCycle())
