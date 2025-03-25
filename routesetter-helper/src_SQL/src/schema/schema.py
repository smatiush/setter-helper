from typing import Optional

from pydantic import BaseModel
from datetime import datetime, date

from enum import Enum

class WallType(str, Enum):
    SLAB = "slab"
    VERTICAL = "vertical"
    OVERHANG = "overhang"

class WallCreate(BaseModel):
    name: str
    location: str
    wall_type: WallType
    description: str | None = None

class WallBase(BaseModel):
    name: str
    location: str
    description: str | None = None


class WallResponse(WallBase):
    wall_id: int
    created_at: datetime
    wall_type: str

    class Config:
        from_attributes = True

class RouteBase(BaseModel):
    name: str
    grade: str
    color: str
    style: str
    wall: Optional[WallResponse] = None
    status: str
    description: str

class RouteCreate(BaseModel):
    name: str
    grade: str
    color: str
    style: str
    wall_id: int  # Assign route to a wall
    setter_id: int
    date_set: date
    status: str = "draft"
    description: str | None = None

class RouteUpdate(RouteBase):
    pass

class RouteResponse(RouteBase):
    route_id: int
    setter_id: int
    date_set: datetime

    class Config:
        from_attributes = True

from pydantic import BaseModel, EmailStr

class SetterBase(BaseModel):
    username: str
    email: EmailStr

class SetterCreate(SetterBase):
    # No password field needed
    pass

class SetterResponse(SetterBase):
    setter_id: int

    class Config:
        from_attributes = True