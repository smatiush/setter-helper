from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src_SQL.src.utils.database import SessionLocal
from src_SQL.src.model.models import Route, Wall
from src_SQL.src.schema.schema import RouteCreate, RouteResponse, RouteUpdate
from src_SQL.src.utils import CRUD as crud

router = APIRouter()

def get_session_local():
    yield SessionLocal()

@router.get("/", response_model=list[RouteResponse])
def get_routes(status: str = None, db: Session = Depends(get_session_local)):
    return crud.get_routes(db, status)

@router.post("/", response_model=RouteResponse)
def create_route(route: RouteCreate, db: Session = Depends(get_session_local)):
    # Verify the wall exists
    db_wall = db.query(Wall).filter(Wall.wall_id == route.wall_id).first()
    if not db_wall:
        raise HTTPException(status_code=404, detail="Wall not found")
    return crud.create_route(db, route)

@router.put("/{route_id}", response_model=RouteResponse)
def update_route(route_id: int, route: RouteUpdate, db: Session = Depends(get_session_local)):
    db_route = crud.update_route(db, route_id, route)
    if not db_route:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route

@router.delete("/{route_id}", response_model=RouteResponse)
def archive_route(route_id: int, db: Session = Depends(get_session_local)):
    db_route = crud.archive_route(db, route_id)
    if not db_route:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route

@router.get("/by-wall/{wall_id}", response_model=list[RouteResponse])
def get_routes_by_wall(wall_id: int, db: Session = Depends(get_session_local)):
    routes = db.query(Route).filter(Route.wall_id == wall_id).all()
    if not routes:
        raise HTTPException(status_code=404, detail="No routes found for this wall")
    return routes
