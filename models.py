from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # Importa Base desde tu archivo database.py

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
