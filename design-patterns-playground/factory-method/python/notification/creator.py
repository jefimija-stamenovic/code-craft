from abc import ABC, abstractmethod
from notification import *

class CreatorNotification(ABC): 

    @abstractmethod
    def create_notification(self) -> Notification: 
        pass 

    def notify(self, message: str) -> None: 
        notification: Notification = self.create_notification()
        notification.send(message)

class CreatorNotificationEmail(CreatorNotification): 

    def create_notification(self) -> Notification:
        return NotificationEmail()
    
class CreatorNotificationSMS(CreatorNotification): 
    
    def create_notification(self) -> Notification:
        return NotificationSMS()