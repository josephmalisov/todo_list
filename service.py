from models import ToDoModel
import json


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        
    def create(self, params):
        self.model.create(params)

    def listStuff(self, url):
        response = self.model.list_items(url)
        return response

    def deleteItem(self, myid):
        response = self.model.deleteItem(int(myid))
        return response

    def checkItem(self, myid):
        response = self.model.checkItem(int(myid))
        return response

    def updateItem(self, myItem):
        response = self.model.updateItem(myItem)
        return response