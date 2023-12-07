import os
import datetime as dt

def search_mp3(parent_dir:str):
    years_dirs = os.listdir(parent_dir)
    list = []
    for year in years_dirs:                                             #ГОД
        #print(year)
        if year == "temp":
            continue
        months_dirs = os.listdir(f"{parent_dir}/{year}")
        
        for month in months_dirs:                                       #МЕСЯЦ
            #print("--" + month)
            files_path = os.listdir(f"{parent_dir}/{year}/{month}") 
            #print(f"----{files_path}")
        
            for file in files_path:                                     #Фаил 
                mp3_path = f"{parent_dir}/{year}/{month}/{file}"  
                list.append(mp3_path)

    print(f"[поиск]Нашел файлов в корневой папке: {len(list)}\n[поиск][вывод]list:")
    for i in list:
        print(i)
    return list



def inputSearch():
    searchOPT = int(input("Выберите где будет осуществляться поиск [1] за отдельный месяц, [2] за отдельный день, [3] за промежуток\n"))
    if searchOPT == 1: #месяц
        date = input("Месяц в формате 'мм.гггг'\n")
    elif searchOPT == 2: #день
        date = input("Дата в формате 'дд.мм.гггг'\n")
    elif searchOPT == 3: #промежуток
        date = input("Дата в формате 'дд.мм.гггг-дд.мм.гггг'\n")
    else:
        raise KeyError("inputSearch")

    return searchOPT, date



def test(parent_dir:str, opt:int, date:str):
    finalList = []

    match opt:
        case 1: #месяц
            month = date.split(".")[0]         
            year = date.split(".")[1]
            
            for dirpath,dirname,filename in os.walk(top="files"):
                try:
                    if dirpath.split("/")[-2] == month and dirpath.split("/")[-3] == year:
                        paths = []
                        for file in filename:
                            paths.append(f"{dirpath}/{file}")
                        finalList += paths
                except IndexError:
                    continue    

        case 2: #день
            day = date.split(".")[0]   
            month = date.split(".")[1]         
            year = date.split(".")[2]
            
            for dirpath,dirname,filename in os.walk(top="files"):
                try:
                    if dirpath.split("/")[-1] == day and dirpath.split("/")[-2] == month and dirpath.split("/")[-3] == year:
                        paths = []
                        for file in filename:
                            paths.append(f"{dirpath}/{file}")
                        finalList += paths
                except IndexError:
                    continue
            pass

        case 3: #промежуток
            first_date_str = date.split("-")[0]  
            first_date = dt.datetime.strptime(first_date_str, "%d.%m.%Y")

            second_date_str = date.split("-")[1]
            second_date = dt.datetime.strptime(second_date_str, "%d.%m.%Y")

            for dirpath,dirname,filename in os.walk(top="files"):
                try:
                    if len(dirpath.split("/")) == 4:
                        dirpath_date = dirpath.split("/")
                        day = dirpath_date[-1]
                        month = dirpath_date[-2]
                        year = dirpath_date[-3]
                        filedata_str = f"{day}.{month}.{year}"
                        filedata = dt.datetime.strptime(filedata_str, "%d.%m.%Y")
                        if first_date <= filedata and filedata <= second_date:
                            
                            print("wwwww")
                            paths = []
                            for file in filename:
                                paths.append(f"{dirpath}/{file}")
                            finalList += paths
                except Exception:
                    print(Exception)
                    continue

            pass


    print(f"[search]Нашел файлов: {len(finalList)}")
    print(finalList)
    return finalList

                    # if int(dirpath.split("/")[-3]) >= int(year_first) and int(dirpath.split("/")[-3]) <= int(year_second): 
                    #     print("год")
                    #     if int(dirpath.split("/")[-2]) >= int(month_first) and int(dirpath.split("/")[-2]) <= int(month_second):
                    #         print("месяц")
                    #         if int(dirpath.split("/")[-1]) >= int(day_first) and int(dirpath.split("/")[-1]) <= int(day_second):

# for dirpath,dirname,filename in os.walk(top="files"):
#     print("dirpath: ",dirpath)
#     print("    dirname: ",dirname)
#     print("        filename: ",filename,"\n")

if __name__ == "__main__":
    #search_mp3("files")
    opt,date = inputSearch()
    test("files", opt, date)
    pass


