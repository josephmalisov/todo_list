# import sqlite3
import os
import json
import pandas as pd
import psycopg2
import string
import random

DATABASE_URL = os.environ['DATABASE_URL']

#TODO: ENFORCE MAX LENGTHS

ID_COLUMN = "id"
TITLE_COLUMN = "title"
DESCRIPTION_COLUMN = "description"
IS_DONE_COLUMN = "_is_done"
IS_DELETED_COLUMN = "_is_deleted"
CREATED_ON_COLUMN = "created"
DUE_DATE_COLUMN = "due"
USER_ID_COLUMN = "userid"
LIST_COLUMN = "list"

config = open("config.json")
db_info = json.load(config)
config.close()

# TODO: Create Class Schema

class ToDoModel:
    TABLENAME = "todo"

    def __init__(self):
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        self.cursor = cursor = self.conn.cursor()

    def create(self, params):
        # TODO: fix the user auth
        username = params["username"] 
        text = params["text"]
        description= params["description"]
        mylist = params["list"]
        query = f'insert into "{self.TABLENAME}" ' \
                f'({TITLE_COLUMN}, {DESCRIPTION_COLUMN}, {USER_ID_COLUMN}, {LIST_COLUMN}) ' \
                f"values ('{text}','{description}','{1}','{mylist}');"
        print("\n\n")
        print(query)
        print("\n\n")

        result = self.cursor.execute(query)
        self.conn.commit()
        # self.conn.commit()

        print("\n\n")
        print(result)
        print("\n\n")

        df = pd.read_sql_query(f"SELECT * from {self.TABLENAME};", self.conn)
        print("\n\n")
        print(df)
        print("\n\n")

        return result
   
    def deleteItem(self, params):
        myId = params["id"]
        query = f'DELETE from "{self.TABLENAME}"' \
                f' WHERE id = {myId}'

        result = self.cursor.execute(query)
        self.conn.commit()
        return ""

    def list_items(self, url):
        query = f"SELECT * " \
                f'from "{self.TABLENAME}" WHERE _is_deleted != TRUE AND ' \
                f" list = '{url}'"
        print (query)
        # result_set = self.conn.execute(query).fetchall()
        # result = [{column: row[i]
        #           for i, column in enumerate(result_set[0].keys())}
        #           for row in result_set]
        df = pd.read_sql_query(query, self.conn)
        self.conn.commit()
        print(df) #just for displaying the result
        result = df.to_json()
        return result

    def checkItem(self, myId):
        query = f'UPDATE "{self.TABLENAME}" SET _is_done = NOT _is_done' \
                f' WHERE id = {myId}'

        result = self.cursor.execute(query)
        self.conn.commit()

        print(f"\nUpdated {myId}")

        return ""

    def updateItem(self, myItem):
        query = f'UPDATE "{self.TABLENAME}" SET' \
            f' {ID_COLUMN} = {myItem[ID_COLUMN]},' \
            f" {TITLE_COLUMN} = '{myItem[TITLE_COLUMN]}'," \
            f" {DESCRIPTION_COLUMN} = '{myItem[DESCRIPTION_COLUMN]}'" \
            f' WHERE {ID_COLUMN} = {myItem[ID_COLUMN]}'

        result = self.cursor.execute(query)
        self.conn.commit()

        print(f"\nUpdated #{myItem[ID_COLUMN]}")

        return ""

class UserModel:
    TABLENAME = "User"

    def create(self, name, email):
        query = f'insert into "{self.TABLENAME}" ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.cursor.execute(query)
        return result

class urlModel:
    TABLENAME = "list"
    # TODO: what if list with this url already exists, or the url is a route

    def __init__(self):
        self.conn = psycopg2.connect(user = db_info["user"],
                                  password = db_info["password"],
                                  host = db_info["host"],
                                  port = db_info["port"],
                                  database = db_info["database"],
                                  sslmode = 'require')
        self.cursor = cursor = self.conn.cursor()
    
    def create(self):
        randomURL = get_random_string(10)
        query = f'insert into "{self.TABLENAME}" ' \
                f'(url) ' \
                f"values ('{randomURL}')"
        result = self.cursor.execute(query)
        self.conn.commit()
        print(query)
        print(result)
        return randomURL

    def url_checker(self, url):
        # query = f'select * from "{self.TABLENAME}" ' \
        #         f"where url = '{url}'"
        # result = self.cursor.execute(query)

        query = f"SELECT * " \
                f'from "list" WHERE ' \
                f" url = '{url}'"
        print (query)
        # result_set = self.conn.execute(query).fetchall()
        # result = [{column: row[i]
        #           for i, column in enumerate(result_set[0].keys())}
        #           for row in result_set]
        df = pd.read_sql_query(query, self.conn)
        print(df)

        self.conn.commit()
        print(query)
        print(df)
        if (not df.empty):
            return True
        else:
            return False
    
def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string is:", result_str)
    return result_str
