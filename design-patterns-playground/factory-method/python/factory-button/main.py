from client import Client
from dialog import *
from typing import List

if __name__ == "__main__": 
    dialogs : List[Dialog] = [
        DialogWindows(), 
        DialogMacOS(), 
        DialogLinux()
    ]
    client: Client = Client()
    for dialog in dialogs:
        client.call_dialog(dialog)