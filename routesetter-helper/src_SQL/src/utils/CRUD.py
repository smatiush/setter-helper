from sqlalchemy.orm import Session
from src.model import models
from src.schema import schema as schemas

def create_wall(db: Session, wall: schemas.WallCreate):
    db_wall = models.Wall(**wall.dict())
    db.add(db_wall)
    db.commit()
    db.refresh(db_wall)
    return db_wall

# Get all walls
def get_walls(db: Session):
    return db.query(models.Wall).all()


# Get a wall by ID
def get_wall(db: Session, wall_id: int):
    return db.query(models.Wall).filter(models.Wall.wall_id == wall_id).first()

# Update a wall
def update_wall(db: Session, wall_id: int, wall: schemas.WallCreate):
    db_wall = get_wall(db, wall_id)
    if db_wall:
        for key, value in wall.dict().items():
            setattr(db_wall, key, value)
        db.commit()
        db.refresh(db_wall)
    return db_wall

# Delete a wall
def delete_wall(db: Session, wall_id: int):
    db_wall = get_wall(db, wall_id)
    if db_wall:
        db.delete(db_wall)
        db.commit()
    return db_wall

def create_route(db: Session, route: schemas.RouteCreate):
    db_route = models.Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

# Get all routes
def get_routes(db: Session, status: str = None):
    query = db.query(models.Route)
    if status:
        query = query.filter(models.Route.status == status)
    return query.all()

# Update a route
def update_route(db: Session, route_id: int, route: schemas.RouteUpdate):
    db_route = db.query(models.Route).filter(models.Route.route_id == route_id).first()
    if db_route:
        for key, value in route.dict().items():
            setattr(db_route, key, value)
        db.commit()
        db.refresh(db_route)
    return db_route

# Soft delete a route (archive)
def archive_route(db: Session, route_id: int):
    db_route = db.query(models.Route).filter(models.Route.route_id == route_id).first()
    if db_route:
        db_route.status = "archived"
        db.commit()
        db.refresh(db_route)
    return db_route

def create_setter(db: Session, setter: schemas.SetterCreate):
    # Create a new setter with no password (or a default value)
    db_setter = models.Setter(
        username=setter.username,
        email=setter.email,
        password_hash=""  # Store an empty string or a default value
    )
    db.add(db_setter)
    db.commit()
    db.refresh(db_setter)
    return db_setter

def delete_setter(db: Session, setter_id: int):
    db_setter = db.query(models.Setter).filter(models.Setter.setter_id == setter_id).first()
    if db_setter:
        db.delete(db_setter)
        db.commit()
    return db_setter

def get_setters(db: Session):
    return db.query(models.Setter).all()