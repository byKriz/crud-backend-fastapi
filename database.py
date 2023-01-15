from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Crea un motor de base de datos SQLite con el nombre del archivo "todooo.db"
engine = create_engine("sqlite:///todooo.db")

# Crea una clase base declarativa para las tablas de la base de datos
Base = declarative_base()

# Define la clase To Do heredando de Base


class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(50))
