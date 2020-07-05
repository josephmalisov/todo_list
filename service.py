from models import ToDoModel


class ToDoService:
    def __init__(self):
        self.model = ToDoModel()
        
    def create(self, params):
        self.model.create(params["text"], params["description"])

    def listStuff(self):
        response = self.model.list_items()
        return response