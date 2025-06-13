from abc import ABC, abstractmethod

# ------ Product Interface ------
class Button(ABC): 
    @abstractmethod
    def render(self) -> str: 
        pass 

    @abstractmethod
    def on_click(self) -> None: 
        pass 

# ------ Concrete Product A ------
class ButtonWindows(Button): 
    def render(self) -> str: 
        return "Rendering WINDOWS button"

    def on_click(self) -> None: 
        print("Button Windows clicked!")

# ------ Concrete Product B ------
class ButtonMacOS(Button): 
    def render(self) -> str: 
        return "Rendering MacOS button"

    def on_click(self) -> None: 
        print("Button MacOS clicked!")

# ------ Concrete Product C ------
class ButtonLinux(Button): 
    def render(self) -> str: 
        return "Rendering Linux button"

    def on_click(self) -> None: 
        print("Button Linux clicked!")