import subprocess
import sys


def launch():
    data = sys.argv[1][len("quazipanacea://") :]

    colon_index = data.index(":") if ":" in data else -1
    root_url = "http://localhost:8080"

    if data is None or colon_index == -1:
        subprocess.run(["xdg-open", f"{root_url}"])
    else:
        subprotocol = data[0:colon_index]
        argument = data[colon_index + 1]

        subprocess.run(["xdg-open", f"{root_url}/q?={subprotocol}"])
