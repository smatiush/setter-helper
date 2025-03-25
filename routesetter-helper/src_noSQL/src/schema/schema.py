# src/schema/schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Wall(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: Optional[datetime] = None

class WallUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
