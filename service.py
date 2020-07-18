from models import ToDoModel, urlModel
import json


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        self.url = urlModel()
        
    def create(self, params):
        self.model.create(params)

    def listStuff(self, url):
        response = self.model.list_items(url)
        return response

    def deleteItem(self, params):
        response = self.model.deleteItem(params)
        return response

    def checkItem(self, myid):
        response = self.model.checkItem(int(myid))
        return response

    def updateItem(self, myItem):
        response = self.model.updateItem(myItem)
        return response

    def newList(self):
        return self.url.create()

    def url_checker(self, url): 
        if (self.url.url_checker(url)):
            return True
        else:
            return False