from creator import CreatorNotification

class Client: 
    def notify(self, creator: CreatorNotification, message:str) -> None: 
        creator.notify(message)