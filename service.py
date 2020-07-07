from models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        
    def create(self, params):
        self.model.create(params["text"], params["description"])

    def listStuff(self):
        response = self.model.list_items()
        return response

    def deleteItem(self, myid):
        response = self.model.deleteItem(int(myid))
        return response

    def checkItem(self, myid):
        response = self.model.checkItem(int(myid))
        return response