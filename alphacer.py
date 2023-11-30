#!/usr/bin/env python3

import asyncio
import websockets
import json



async def recognizerALPHACER(uri:str, mp3file=str): 
    file_name = mp3file.split("/")[-1][:-4]
    async with websockets.connect(uri) as websocket:

        proc = await asyncio.create_subprocess_exec(                        #инициация процесса
        'ffmpeg', '-nostdin', '-loglevel', 'quiet', '-i', mp3file,
        '-ar', '16000', '-ac', '1', '-f', 's16le', '-',
        stdout=asyncio.subprocess.PIPE)

        await websocket.send('{ "config" : { "sample_rate" : 16000 } }')

        text = ""
        while True:                                                     #websocet цикл рекогнайза
            data = await proc.stdout.read(4000)

            if len(data) == 0:
                break

            await websocket.send(data)
            received1 = json.loads(await websocket.recv())

            if "result" in received1.keys():
                text = text + " " + received1["text"]
                

        await websocket.send('{"eof" : 1}')
        received = json.loads(await websocket.recv())
        text = text + " " + received["text"]    
        
        await proc.wait()
        
                                        
    print(f"\n\n\n[VOSK/Alphacer][{file_name}]Output:")          #main вывод текста
    print(f"{file_name}:{text}")
    return text
        



######################################################test#####################################################
if __name__ == "__main__":
    pass


