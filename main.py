# from typing import Union

from fastapi import FastAPI, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Crea un motor de base de datos SQLite con el nombre del archivo "todooo.db"
engine = create_engine("sqlite:///todooo.db")

# Crea una clase base declarativa para las tablas de la base de datos
Base = declarative_base()

#Define la clase To Do heredando de Base
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(50))


# Crea las tablas necesarias en la base de datos
Base.metadata.create_all(engine)

# Crea una instancia de la clase FastAPI
app = FastAPI()


@app.get("/")
async def read_root():
    return "todooo"


@app.post("/todo")
def create_todo():
    return "create todo item"


@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"


@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"


@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"


@app.get("/todo")
def read_todo_list():
    return "read todo list"

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
