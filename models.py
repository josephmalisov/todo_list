import sqlite3
import pandas as pd
import psycopg2
import string
import random

ID_COLUMN = "id"
TITLE_COLUMN = "title"
DESCRIPTION_COLUMN = "description"
IS_DONE_COLUMN = "_is_done"
IS_DELETED_COLUMN = "_is_deleted"
CREATED_ON_COLUMN = "created"
DUE_DATE_COLUMN = "due"
USER_ID_COLUMN = "userid"

# class Schema:
#     def __init__(self):
#         self.conn = sqlite3.connect('todo.db')
#         self.create_user_table()
#         self.create_to_do_table()
#         # user table must be created first b/c of foreign key

#     def __del__(self):
#         # body of destructor
#         self.conn.commit()
#         self.conn.close()

#     def create_to_do_table(self):

#         query2 = """
        
#         CREATE TABLE IF NOT EXISTS "Todo" (
#           id INTEGER PRIMARY KEY,
#           Title TEXT,
#           Description TEXT,
#           _is_done boolean DEFAULT 0,
#           _is_deleted boolean DEFAULT 0,
#           CreatedOn Date DEFAULT CURRENT_DATE,
#           DueDate Date,
#           UserId INTEGER FOREIGNKEY REFERENCES User(_id)
#         );
#         """

#         self.conn.execute(query2)

#     def create_user_table(self):
#         query = """
#         CREATE TABLE IF NOT EXISTS "User" (
#         _id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         Name TEXT NOT NULL, 
#         Email TEXT, 
#         CreatedOn Date default CURRENT_DATE
#         );
#         """
#         self.conn.execute(query)


class ToDoModel:
    TABLENAME = "todo"

    def __init__(self):
        self.conn = psycopg2.connect(user = "azbqralazbwyxa",
                                  password = "0206a0e69bbd6645722f471b1997afdefb56e3d4bac73044a69e7859d54efaca",
                                  host = "ec2-54-211-210-149.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "d8trkkj3bm36c9")
        self.cursor = cursor = self.conn.cursor()

    def create(self, params):
        # TODO: fix the user auth
        username = params["username"] 
        text = params["text"]
        description= params["description"]
        mylist = params["list"]
        query = f'insert into "{self.TABLENAME}" ' \
                f'("Title", "Description", "UserId", "list") ' \
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

        df = pd.read_sql_query('SELECT * from "Todo";', self.conn)
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
        self.conn = psycopg2.connect(user = "azbqralazbwyxa",
                                  password = "0206a0e69bbd6645722f471b1997afdefb56e3d4bac73044a69e7859d54efaca",
                                  host = "ec2-54-211-210-149.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "d8trkkj3bm36c9")
        self.cursor = cursor = self.conn.cursor()
    
    def create(self):
        randomURL = get_random_string(15)
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
