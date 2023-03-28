import json
from random import randrange
from locust import HttpUser, between, task

class readFile():
    def __init__(self):
        self.data = []

    def getData(self):
        size = len(self.data)
        if size > 0:
            index = randrange(0, size - 1) if size > 1 else 0
            return self.data.pop(index)
        else:
            print("size -> 0")
            return None
    
    def loadFile(self):
        print("LOADING ...")
        try:
            with open("datos.json", 'r') as file:
                self.data = json.loads(file.read())
        except Exception:
            print(f'Error : {Exception}')

class trafficData(HttpUser):
    wait_time = between(0.1, 0.9) #Tiempo de espera entre registros
    reader = readFile()
    reader.loadFile()

    def on_start(self):
        print("On Start")
    
    @task
    def sendMessage(self):
        data = self.reader.getData()
        print("*********************************")
        print(data)
        if data is not None:
            res = self.client.post("http://localhost:3000/add", json=data)
            print(res)
            response = res.json()
            print(response)
        else:
            print("Empty")
            self.stop(True)