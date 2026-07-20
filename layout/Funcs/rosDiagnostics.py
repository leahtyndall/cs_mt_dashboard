import websocket
import json
import threading
from playwright.sync_api import sync_playwright
import time

#add gesture recognition??
#import yolo
#publish results(labels ect) to a new topic

ROS_IP = "192.168.30.39"  
signal = None

def on_message(ws, message):
    global signal
    data = json.loads(message)
    if data.get("topic") == "/diagnostics":
        for status in data["msg"]["status"]:
            for kv in status.get("values", []):
                if kv["key"] == "Signal Level":
                    signal = kv["value"]

#find fps of stream over websocket

def on_open(ws):
    # subscribe to topic
    subscribe_msg = {
        "op": "subscribe",
        "topic": "/diagnostics"
    }
    ws.send(json.dumps(subscribe_msg))

ws = websocket.WebSocketApp(
    f"ws://{ROS_IP}:9090",
    on_message=on_message,
    on_open=on_open
)

wst=threading.Thread(target=ws.run_forever)
wst.daemon = True
wst.start()


def getsignal():
    global signal
    while signal is None:
        time.sleep(1)
  
    signal = signal.replace('dBm', '')
    signal = signal.replace('-','')
    return signal

