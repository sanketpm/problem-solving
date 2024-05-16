'''
Behavioural Pattern:

Observer Pattern can also be called Pub-Sub Pattern

'''

# Producer
class YTChannel:
    def __init__(self, name):
        self.__name = name
        self.__subs = []
    
    def addSubsriber(self, new_sub):
        self.__subs.append(new_sub)
    
    def notify(self, event):
        for sub in self.__subs:
            sub.sendNotification(self.__name, event)

# Subscriber
from abc import ABC, abstractmethod
class YTSubscriber(ABC):
    @abstractmethod
    def sendNotification(self):
        pass

class YTUser(YTSubscriber):
    def __init__(self, name):
        self.name = name 
    
    def sendNotification(self, channel, event):
        print(f'User {self.name} received notification from {channel}: {event}')

u1 = YTUser('u1')
u2 = YTUser('u2')
u3 = YTUser('u3')

channel = YTChannel('NeetCode')

channel.addSubsriber(u1)
channel.addSubsriber(u2)
channel.addSubsriber(u3)

channel.notify('a new video released')