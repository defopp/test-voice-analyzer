import os

def search_mp3(parent_dir:str):
    months_dirs = os.listdir(parent_dir)
    list = []
    for dir in months_dirs:        #subdir path
        files_path = os.listdir(f"{parent_dir}/{dir}") 
        
        for file in files_path:
            mp3_path = f"{parent_dir}/{dir}/{file}"  #mp3 path
            list.append(mp3_path)
    print(f"Нашел {len(list)} файлов")
    return list
