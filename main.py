from config import *
from data_handler.convert import *
from data_handler.search import *
from data_handler.analyzer import *
from api.session_handler import *   
from crt import *
from alphacer import*

#выберите тип поиска
opt,date = inputSearch()
mp3_files = search_mp3("files", opt, date)
#выберите тип анализа
type_of_search = int(input("[1] - Подсчет листа слов(вместе) //слово1,слово2,слово3 - количество упоминаний \n[2] - Подсчет листа слов(отдельно) //слов1 - количество раз //слов2 - количество раз \nВыберите тип распознавания: "))

#####доеделать#####напишите слова для поиска(строго в нижнем регистре)
phrase_to_search = ["мрт","врач","ренген","рэп","здравствуйте","нет","да","прием"]
#phrase_to_search = ["мрт","нет","да","прием"]



def crtCycle(mp3_files:list) -> dict:                                                                                  
    
    session_id = start_session(domain_id=domain,password=password,username=username)  

    now = 1
    end = len(mp3_files)

    finalAnalyze = {}  
    for mp3_file in mp3_files:    
        print(f"\n{now} из {end}")                              
        filename, text = recognizerCRT(mp3file=mp3_file, session_id=session_id)                                         
         
        print(f"Цикл рекогнайза {filename} завершен")
        fileAnalyze = search_words(opt=type_of_search, words=phrase_to_search, text=text)
        finalAnalyze = (dictSum(finalAnalyze,fileAnalyze)) 

        now += 1
    print("__"*60+f"\n[ВЫВОД]crtCycle[всего найдено]: \n{finalAnalyze}\n"+"__"*60)
    stop_session(session_id)                                             
    return fileAnalyze   



async def alphacerCycle(mp3_files:list) -> dict: ###########################################################################################################
    
    now = 1
    end = len(mp3_files)

    finalAnalyze = {}
    for mp3_path in mp3_files:################################################################Перебор mp3 в РЕКОГНАЙЗ
        print(f"\n{now} из {end}")  
        file_name, text = await recognizerALPHACER(uri = uri,mp3file=mp3_path)

        fileAnalyze = search_words(opt=type_of_search,words=phrase_to_search, text=text)
        finalAnalyze = (dictSum(finalAnalyze,fileAnalyze)) 

        now += 1
    print(f"\n[ВЫВОД]alphacerCycle[всего найдено]: {finalAnalyze}\n\n")
    return fileAnalyze



if __name__ == "__main__":
    #crtCycle(mp3_files)
    asyncio.run(alphacerCycle(mp3_files))
    

















###################### оптимизировать #######################################################

# async def alphacerCycle(mp3_files:list) -> dict: ###########################################################################################################
    
#     WAV_files = []
#     for path in mp3_files:                                               #Конверт файлов в WAV
#         WAV_files.append(mp3_to_wav(path=path))
    
    
#     finalAnalyze = {}
#     for wav_path in WAV_files:################################################################Перебор WAV в РЕКОГНАЙЗ
#         file_name, text = await recognizerALPHACER(uri = uri,mp3file=wav_path)

#         fileAnalyze = search_words(opt=type_of_search,words=phrase_to_search, text=text)
#         finalAnalyze.update(dictSum(finalAnalyze,fileAnalyze))

#     print(f"Вывод alphacerCycle [всего]: {finalAnalyze}")
#     print("[Цикл рекогнайза Alphacer завершен]\n\n\n")
#     return fileAnalyze