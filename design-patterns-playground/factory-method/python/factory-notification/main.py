from creator import * 
from client import Client
from typing import List, Tuple

creator_email: CreatorNotificationEmail = CreatorNotificationEmail()
creator_sms : CreatorNotificationSMS = CreatorNotificationSMS()

if __name__ == "__main__":
    client: Client = Client()

    creators: List[Tuple[CreatorNotification, str]] = [
        (CreatorNotificationEmail(), "Hello from Factory Method Pattern!"), 
        (CreatorNotificationSMS(), "Hello from Factory Method Pattern!")
    ]
    for creator, message in creators: 
        client.notify(creator, message)