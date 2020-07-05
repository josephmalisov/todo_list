import sqlite3
import pandas as pd


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
                f'values ("{text}","{description}")'
        
        result = self.conn.execute(query)
        df = pd.read_sql_query("SELECT * from Todo", self.conn)
        print("\n\n")
        print(df)
        print("\n\n")

        return result
   
    def delete(self, myId):
        query = f'DELETE from {TABLENAME}' \
                f'WHERE id = "{myId}"'

        result = self.conn.execute(query)
        return result

    def list_items(self, where_clause=""):
        query = f"SELECT id, Title, Description, DueDate, _is_done " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
        print (query)
        # result_set = self.conn.execute(query).fetchall()
        # result = [{column: row[i]
        #           for i, column in enumerate(result_set[0].keys())}
        #           for row in result_set]
        df = pd.read_sql_query(query, self.conn)
        result = df.to_json()
        return result


class User:
    TABLENAME = "User"

    def create(self, name, email):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.conn.execute(query)
        return result