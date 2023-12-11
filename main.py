from config import *
from data_handler.convert import *
from data_handler.search import *
from data_handler.analyzer import *
from data_handler.sql import *
from api.session_handler import *   
from crt import *
from alphacer import*



def crtCycle(mp3_files:list) -> dict:                                                                                  
    
    session_id = start_session(domain_id=domain,password=password,username=username)  
    db = MySql_Handler(sql_user,sql_password,sql_database,sql_host)
    
    now = 1
    end = len(mp3_files)

    finalAnalyze = {}  
    
    for mp3_file in mp3_files:    
        try:
            print(f"\n{now} из {end}")                              
            filename, text = recognizerCRT(mp3file=mp3_file, session_id=session_id)                                         
            
            fileAnalyze, was_in= search_words(opt=type_of_search, words=phrase_to_search, text=text)
            finalAnalyze = (dictSum(finalAnalyze,fileAnalyze)) 

            ######################Занасение в базу
            if len(was_in) != 0:
                db.data_in(filename,was_in)
            ######################

        except Exception as ex:
            print(f"[{filename}]{ex}")
        finally:
            now += 1
            continue


    print("__"*60+f"\n[ВЫВОД]crtCycle[всего найдено]: \n{finalAnalyze}\n"+"__"*60)
    stop_session(session_id)                                             
    return fileAnalyze   



async def alphacerCycle(mp3_files:list) -> dict: ###########################################################################################################
    db = MySql_Handler(sql_user,sql_password,sql_database,sql_host)

    now = 1
    end = len(mp3_files)

    finalAnalyze = {}
    for mp3_path in mp3_files:################################################################Перебор mp3 в РЕКОГНАЙЗ
        try:
            print(f"\n{now} из {end}")  
            filename, text = await recognizerALPHACER(uri = uri,mp3file=mp3_path)

            fileAnalyze, was_in= search_words(opt=type_of_search,words=phrase_to_search, text=text)
            finalAnalyze = (dictSum(finalAnalyze,fileAnalyze)) 
            
            ######################Занасение в базу
            if len(was_in) != 0:
                db.data_in(filename,was_in)
            ######################


        except Exception as ex:
            print(f"[{filename}]{ex}")
        finally:
            now += 1
            continue
        
    
    print("__"*60+f"\n[ВЫВОД]alphacerCycle[всего найдено]: \n{finalAnalyze}\n"+"__"*60)
    return fileAnalyze



if __name__ == "__main__":
    #выберите тип поиска
    opt,date = inputSearch() #ВЫБЕРИТЕ ТИП ПОИСКА И ДАТЫ
    mp3_files = search_mp3("files", opt, date) 
    
    #выберите тип анализа
    #type_of_search = int(input("[1] - Подсчет листа слов(вместе) //слово1,слово2,слово3 - количество упоминаний \n[2] - Подсчет листа слов(отдельно) //слов1 - количество раз //слов2 - количество раз \nВыберите тип распознавания: "))
    type_of_search = 2

    #напишите слова для поска, строго в нижнем регистре
    phrase_to_search = ["мрт","врач","ренген","рэп","здравствуйте","нет","да","прием"]
    #phrase_to_search = ["мрт","нет","да","прием"]

    #выберите рекогнайзер
    crtCycle(mp3_files)
    asyncio.run(alphacerCycle(mp3_files))
    
   










