#!/usr/bin/env python3
import json
import struct
import subprocess
import sys


# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    return json.loads(message)

# Encode a message for transmission,
# given its content.
def encodeMessage(messageContent):
    encodedContent = json.dumps(messageContent).encode('utf-8')
    encodedLength = struct.pack('@I', len(encodedContent))
    return {'length': encodedLength, 'content': encodedContent}

# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage['length'])
    sys.stdout.buffer.write(encodedMessage['content'])
    sys.stdout.buffer.flush()

def launchKaxon():
    subprocess.run(['xdg-open', 'https://localhost:3000'])

with open('broker.log', 'a') as f:
    while True:
        receivedMessage = getMessage()

        f.write(receivedMessage + '\n')
        f.flush()

        if ':' in receivedMessage:
            colon_index = receivedMessage.index(':')

            protocol = receivedMessage[:colon_index]
            content = receivedMessage[colon_index+1:]
            if protocol == 'yt-checkid':
                print('fired ' + content)
        else:
            if receivedMessage == "ping":
                sendMessage(encodeMessage("pong3"))
            elif receivedMessage == 'open-kaxon':
                # launchKaxon()
                pass


# with open('log', 'w') as f:
#     while True:
#         receivedMessage = getMessage()
#         f.write(len(receivedMessage))
#         f.flush()

# with open('log', 'w') as f:
#     while True:
#         for line in fileinput.input():
#             print("got line:", line)
