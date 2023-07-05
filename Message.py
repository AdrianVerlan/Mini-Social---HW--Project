from datetime import datetime
from typing import Any

class Message:

    #repository
    all = []

    #entity/instanse
    def __init__(self, body):
        self.__body = body
        self.created = datetime.now()
        self.viwed = None

    def __str__(self):
        return f'\n\t"{self.__body} <{self.created.strftime("%Y-%m-%d %H:%M")}>"\n'
    
    def __repr__(self):
        return self.__str__()
    def __getattr__(self, attr):
        if attr == "body" and self.viwed == None:
            self.viwed = datetime.now()
            return self.__body
    
    def send(body, author,target):
        message = Message(body)
        Message.all.append(message)
    



