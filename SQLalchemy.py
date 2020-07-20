from sqlalchemy import create_engine
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

user = "azbqralazbwyxa"
password = "0206a0e69bbd6645722f471b1997afdefb56e3d4bac73044a69e7859d54efaca"
host = "ec2-54-211-210-149.compute-1.amazonaws.com"
port = "5432"
database = "d8trkkj3bm36c9"

db_string = "postgres://azbqralazbwyxa:0206a0e69bbd6645722f471b1997afdefb56e3d4bac73044a69e7859d54efaca@ec2-54-211-210-149.compute-1.amazonaws.com:5432/d8trkkj3bm36c9"

db = create_engine(db_string)

# meta = MetaData(db)

result_set = db.execute("SELECT * FROM list")  
for r in result_set:  
    print(r)

class Todo(Base):
    __table__ = Table('Todo', Base.metadata,
                    autoload=True, autoload_with=some_engine)