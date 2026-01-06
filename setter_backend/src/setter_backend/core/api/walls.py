from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from setter_backend.src.setter_backend.utils.database import get_session_local
from setter_backend.src.setter_backend.model.models import Wall
from setter_backend.src.setter_backend.schema.schema import WallCreate, WallResponse
from setter_backend.src.setter_backend.utils import CRUD as crud

router = APIRouter()

@router.get("/", response_model=list[WallResponse])
def get_walls(db: Session = Depends(get_session_local)):
    return crud.get_walls(db)

@router.post("/", response_model=WallResponse)
def create_wall(wall: WallCreate, db: Session = Depends(get_session_local)):
    return crud.create_wall(db, wall)

@router.put("/{wall_id}", response_model=WallResponse)
def update_wall(wall_id: int, wall: WallCreate, db: Session = Depends(get_session_local)):
    db_wall = crud.update_wall(db, wall_id, wall)
    if not db_wall:
        raise HTTPException(status_code=404, detail="Wall not found")
    return db_wall

@router.delete("/{wall_id}")
def delete_wall(wall_id: int, db: Session = Depends(get_session_local)):
    db_wall = crud.delete_wall(db, wall_id)
    if not db_wall:
        raise HTTPException(status_code=404, detail="Wall not found")
    return {"detail": "Wall deleted"}
