import os

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

if __name__ == "__main__":
    search_mp3("files")