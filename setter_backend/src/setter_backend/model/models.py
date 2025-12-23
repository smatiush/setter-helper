from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime
import time
from setter_backend.src.setter_backend.utils.database import Base
from enum import Enum


class Setter(Base):
    __tablename__ = "setter"

    setter_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default="route_setter")
    routes = relationship("Route", back_populates="setter")

class WallType(str, Enum):
    SLAB = "slab"
    VERTICAL = "vertical"
    OVERHANG = "overhang"

class Wall(Base):
    __tablename__ = "walls"
    wall_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    location = Column(String, nullable=False)
    wall_type = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)  # Set default timestamp

    routes = relationship("Route", back_populates="wall")

class Route(Base):
    __tablename__ = "routes"
    route_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    grade = Column(String)
    color = Column(String)
    style = Column(String)
    wall_id = Column(Integer, ForeignKey("walls.wall_id"))
    setter_id = Column(Integer, ForeignKey("setter.setter_id"))
    date_set = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="draft")
    description = Column(String)

    wall = relationship("Wall", back_populates="routes")
    setter = relationship("Setter", back_populates="routes")


Setter.routes = relationship("Route", back_populates="setter")
