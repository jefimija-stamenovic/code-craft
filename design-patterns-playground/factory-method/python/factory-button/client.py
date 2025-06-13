from dialog import *

class Client: 
    def call_dialog(self, dialog: Dialog) -> None: 
        dialog.render_window()
        print("---------------------")