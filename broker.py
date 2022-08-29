#!/usr/bin/env python3
import json
import struct
import subprocess
import sys
from urllib import request
import requests

def decodeMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

def sendMessage(s):
    def encode(messageContent):
        encodedContent = json.dumps(messageContent).encode('utf-8')
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}

    encodedMessage = encode(s)
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def launchKaxon():
    subprocess.run(['xdg-open', 'https://localhost:3000'])


while True:
    message = decodeMessage()

    with open('broker.log', 'a') as f:
        f.write(f'message: {json.dumps(message)}\n')

    if isinstance(message, str):
        if ':' in message:
            colon_index = message.index(':')

            protocol = message[:colon_index]
            content = message[colon_index+1:]
            if protocol == 'yt-checkid':
                print('fired ' + content)
        else:
            if message == "ping":
                sendMessage("pong3")
            elif message == 'open-kaxon':
                # launchKaxon()
                pass
    elif isinstance(message, dict):
        typ = message['type'] if 'type' in message else None
        method = message['method'] if 'method' in message else None
        data = message['data'] if 'data' in message else None

        if type == None or method == None:
            f.write('Bad request')

        if type == 'rpc':
            if method == 'has-youtube-id':
                youtubeId = data['id']

                hasNote = True
                requests.post('http://localhost:3000/', {
                    type: 'type-unique',

                })
                sendMessage({
                    'success': True,
                    'hasNote': hasNote
                })

