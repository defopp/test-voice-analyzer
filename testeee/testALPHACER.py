#!/usr/bin/env python3

import asyncio
import websockets
import sys
import json

search_list = ["мрт", "кардиолог", "кардиологу"]


def search_words(data):
    print(data["text"])
    for keys in data:
        for words in data[keys]:
            if isinstance(words, dict):
                if words["word"] in search_list:
                    print(words["word"])


async def run_test(uri):
    async with websockets.connect(uri) as websocket:

        proc = await asyncio.create_subprocess_exec(
            'ffmpeg', '-nostdin', '-loglevel', 'quiet', '-i', sys.argv[1],
            '-ar', '16000', '-ac', '1', '-f', 's16le', '-',
            stdout=asyncio.subprocess.PIPE)

        await websocket.send('{ "config" : { "sample_rate" : 16000 } }')

        while True:
            data = await proc.stdout.read(8000)

            if len(data) == 0:
                break

            await websocket.send(data)
            received1 = json.loads(await websocket.recv())
            print(received1)
            # if "result" in received1:
            #     search_words(received1)

        await websocket.send('{"eof" : 1}')
        received = json.loads(await websocket.recv())
        print(received)
        # if "result" in received:
        #     search_words(received)

        await proc.wait()


asyncio.run(run_test('ws://46.229.71.54:2700'))