#!/usr/bin/env python

import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello server!")
        message = websocket.recv()
        print(f"Received: {message}")
        msg2 = websocket.recv()
        

hello()