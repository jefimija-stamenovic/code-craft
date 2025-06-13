from creator import CreatorNotification

class Client: 
    
    def __init__(self) -> None: 
        self._creator : CreatorNotification | None = None

    def set_creator(self, creator: CreatorNotification) -> None: 
        self._creator = creator

    def notify(self, message:str) -> None: 
        if self._creator is not None: 
            self._creator.notify(message)
        else: 
            raise Exception("Creator is not set!")