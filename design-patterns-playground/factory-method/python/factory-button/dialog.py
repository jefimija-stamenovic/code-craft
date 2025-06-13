from abc import ABC 
from button import *

# --- Abstract Class Creator ---
class Dialog(ABC): 
    def render_window(self) -> None: 
        button: Button = self.create_button()
        print(button.render())
        button.on_click()

    @abstractmethod
    def create_button(self) -> Button: 
        pass 

class DialogWindows(Dialog): 
    def create_button(self) -> Button:
        return ButtonWindows()
    
class DialogMacOS(Dialog): 
    def create_button(self) -> Button:
        return ButtonMacOS()
    
class DialogLinux(Dialog): 
    def create_button(self) -> Button:
        return ButtonLinux()
    