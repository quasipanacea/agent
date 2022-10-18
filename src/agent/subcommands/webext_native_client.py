import json
import struct
import subprocess
import sys
import requests
import argparse

def decodeMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack("@I", rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode("utf-8")
    return json.loads(message)

def sendMessage(s):
    def encode(messageContent):
        encodedContent = json.dumps(messageContent).encode("utf-8")
        encodedLength = struct.pack("@I", len(encodedContent))
        return {"length": encodedLength, "content": encodedContent}

    encodedMessage = encode(s)
    sys.stdout.buffer.write(encodedMessage["length"])
    sys.stdout.buffer.write(encodedMessage["content"])
    sys.stdout.buffer.flush()

def launchKaxon():
    subprocess.run(["xdg-open", "https://localhost:3000"])

def webext_native_client():
    while True:
        message = decodeMessage()

        if isinstance(message, dict):
            typ = message["type"] if "type" in message else None
            method = message["method"] if "method" in message else None
            data = message["data"] if "data" in message else None

            print(typ, method, data)

            if type == "rpc":
                if method == "has-youtube-id":
                    youtubeId = data["id"]

                    hasNote = True
                    requests.post(
                        "http://localhost:3000/",
                        {
                            type: "type-unique",
                        },
                    )
                    sendMessage({"success": True, "hasNote": hasNote})
