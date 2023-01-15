from fastapi import FastAPI, status
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session


# Creando el modelo base de ToDoRequest
class ToDoRequest(BaseModel):
    task: str


# Crea las tablas necesarias en la base de datos
Base.metadata.create_all(engine)

# Crea una instancia de la clase FastAPI
app = FastAPI()


@app.get("/")
async def read_root():
    return "todooo"


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):

    # creando una nueva sesion en la base de datos
    session = Session(bind=engine, expire_on_commit=False)

    # creando una instancia del modelo de todo database
    tododb = ToDo(task=todo.task)

    # agregando una sesión y confirmala
    session.add(tododb)
    session.commit()

    # Recolectar el id del objeto a la base de datos
    id = tododb.id

    # cerrando la session
    session.close()

    return f"create todo item with id: {id}"


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
