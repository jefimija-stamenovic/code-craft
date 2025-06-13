from abc import ABC, abstractmethod

class Notification(ABC): 
    @abstractmethod
    def send(self, message: str) -> None: 
        pass 

class NotificationEmail(Notification): 
    def send(self, message: str) -> None:
        print(f"Sending EMAIL with message: {message}")
        
class NotificationSMS(Notification): 

    def send(self, message: str) -> None:
        print(f"Sending SMS with message: {message}")