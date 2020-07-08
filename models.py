import sqlite3
import pandas as pd

ID_COLUMN = "id"
TITLE_COLUMN = "Title"
DESCRIPTION_COLUMN = "Description"
IS_DONE_COLUMN = "_is_done"
IS_DELETED_COLUMN = "_is_deleted"
CREATED_ON_COLUMN = "CreatedOn"
DUE_DATE_COLUMN = "DueDate"
USER_ID_COLUMN = "UserId"

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # user table must be created first b/c of foreign key

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):

        query2 = """
        
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean DEFAULT 0,
          _is_deleted boolean DEFAULT 0,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query2)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        _id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Name TEXT NOT NULL, 
        Email TEXT, 
        CreatedOn Date default CURRENT_DATE
        );
        """
        self.conn.execute(query)


class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}");'
        print("\n\n")
        print(query)
        print("\n\n")

        result = self.conn.execute(query)
        self.conn.commit()
        # self.conn.commit()

        print("\n\n")
        print(result)
        print("\n\n")

        df = pd.read_sql_query("SELECT * from Todo;", self.conn)
        print("\n\n")
        print(df)
        print("\n\n")

        return result
   
    def deleteItem(self, myId):
        query = f'DELETE from {self.TABLENAME}' \
                f' WHERE id = "{myId}"'

        result = self.conn.execute(query)
        self.conn.commit()
        return ""

    def list_items(self, where_clause=""):
        query = f"SELECT * " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
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
        query = f'UPDATE {self.TABLENAME} SET _is_done = _is_done + 1' \
                f' WHERE id = "{myId}"'

        result = self.conn.execute(query)
        self.conn.commit()

        print(f"\nUpdated {myId}")

        return ""

    def updateItem(self, myItem):
        query = f'UPDATE {self.TABLENAME} SET' \
            f' {ID_COLUMN} = "{myItem[ID_COLUMN]}",' \
            f' {TITLE_COLUMN} = "{myItem[TITLE_COLUMN]}",' \
            f' {DESCRIPTION_COLUMN} = "{myItem[DESCRIPTION_COLUMN]}"' \
            f' WHERE {ID_COLUMN} = "{myItem[ID_COLUMN]}"'

        result = self.conn.execute(query)
        self.conn.commit()

        print(f"\nUpdated #{myItem[ID_COLUMN]}")

        return ""


class User:
    TABLENAME = "User"

    def create(self, name, email):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.conn.execute(query)
        return result