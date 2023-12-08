def search_words(opt:int,words:list, text:str) -> dict:
    word_list = text.lower().replace(".","").replace(",","").split() #форматирование текста в лист слов нижнего регистра без "," и "."
    

    
    match opt:
        case 1:  ################################################################################## 1 - Подсчет листа слов(вместе)    //слово1,слово2,слово3 - количество упоминаний
            dict = {}
            dict[str(words)] = 0
            for i in word_list:                                 #перебор слов                       
                if i in words:
                    dict[str(words)] += 1                    

            print(f"[АНАЛИЗ]Найдено: {dict}")
            return dict
        
        case 2:  ################################################################################## 2 - Подсчет листа слов(Отдельно) //слов1 - количество раз 
            dict = {}                                                                                                               #//слов2 - количество раз 
            for word in words:                                                                                                       
                dict[word] = 0

            for i in word_list:
                if i in dict.keys():
                    dict[i] += 1

            print(f"[АНАЛИЗ]Найдено: {dict}")
            return dict
        
        case _:
            raise IndexError("[АНАЛИЗ] Введен неверный тип Анализатора")



def dictSum(dict1, dict2)->dict:
    for i in dict2:
        try:
            dict1[i] += dict2[i]
        except KeyError:
            dict1[i] = dict2[i]
    return dict1
    


