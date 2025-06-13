from creator import * 
from client import Client

creator_email: CreatorNotificationEmail = CreatorNotificationEmail()
creator_sms : CreatorNotificationSMS = CreatorNotificationSMS()

if __name__ == "__main__":
    client: Client = Client()

    print("============================")
    client.set_creator(creator_email)
    client.notify("Hello from Factory Method Pattern!")

    print("============================")
    client.set_creator(creator_sms) 
    client.notify("Hello from Factory Method Pattern!")