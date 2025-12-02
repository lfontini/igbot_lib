from abc import ABC, abstractmethod

class Device:
    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    @abstractmethod
    def connect(self):
        pass