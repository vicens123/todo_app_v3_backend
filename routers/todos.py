from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schema import ToDoRequest, ToDoResponse
from database import SessionLocal
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=List[ToDoResponse])
def get_todos(completed: bool = None, db: Session = Depends(get_db)):
    return crud.read_todos(db, completed)

@router.get("/todos/{id}", response_model=ToDoResponse)
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="To-do no encontrado")
    return todo

@router.post("/todos", response_model=ToDoResponse)
def create(todo: ToDoRequest, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.put("/todos/{id}", response_model=ToDoResponse)
def update(id: int, todo: ToDoRequest, db: Session = Depends(get_db)):
    updated = crud.update_todo(db, id, todo)
    if updated is None:
        raise HTTPException(status_code=404, detail="To-do no encontrado")
    return updated

@router.delete("/todos/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_todo(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="To-do no encontrado")
    return {"message": "To-do eliminado"}
