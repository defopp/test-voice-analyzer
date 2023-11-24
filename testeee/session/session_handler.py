import requests



def start_session(domain_id:int, password:str, username:str, url="https://cloud.speechpro.com/vksession/rest/session"): 
    json = {
    "domain_id": domain_id,
    "password": password,
    "username": username
    }                                                        #Создание сессии

    response = requests.post(url=url, json=json).json()           #(get)запрос создания
    print(f"Сессия создалась:   {response}")                      #эхо
    session_id = response.get("session_id")
    session_status(session_id)                                    #запрос статуса   
    return session_id


def session_status(session_id:str, url="https://cloud.speechpro.com/vksession/rest/session"): #Статус сессии
    header = {"X-Session-Id":session_id}

    response = requests.get(url=url,headers=header).json()                                        #запрос статуса
    return print(f"Статус сессии:      {response}")                                                      #эхо


def stop_session(session_id:str, url="https://cloud.speechpro.com/vksession/rest/session"): #Закрытие сессии
    header = {"X-Session-Id":session_id}

    response = requests.delete(url=url,headers=header)                                           #(del)запрос закрытия
    print(f"Сессия закрыта:      {response}")
    return session_status(session_id)                                                                   #запрос статуса


def check_available_models(session_id:str, url="https://cloud.speechpro.com/vkasr/rest/v2/models"):
    header = {"X-Session-Id":session_id}

    response = requests.get(url=url, headers=header).json()
    count = 1
    for i in response:
        print(f"[{count}] {i}")
        count += 1