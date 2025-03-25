from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.utils.database import SessionLocal
from src.schema import schema as schemas
from src.utils import CRUD as crud

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.get("/", response_model=List[schemas.SetterResponse])
def get_setters(db: Session = Depends(get_session_local)):
    return crud.get_setters(db)

@router.post("/", response_model=schemas.SetterResponse)
def create_setter(setter: schemas.SetterCreate, db: Session = Depends(get_session_local)):
    return crud.create_setter(db, setter)

@router.delete("/{setter_id}", response_model=schemas.SetterResponse)
def delete_setter(setter_id: int, db: Session = Depends(get_session_local)):
    db_setter = crud.delete_setter(db, setter_id)
    if not db_setter:
        raise HTTPException(status_code=404, detail="Setter not found")
    return db_setter
