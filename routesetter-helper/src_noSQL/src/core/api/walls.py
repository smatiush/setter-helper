from fastapi import APIRouter, HTTPException
from src_noSQL.src.utils.database import db
from src_noSQL.src.schema.schema import Wall
from bson.objectid import ObjectId

router = APIRouter()

@router.post("/walls", response_model=dict)
async def create_wall(wall: Wall):
    wall_data = wall.dict()
    result = db.walls.insert_one(wall_data)
    return {"id": str(result.inserted_id)}

@router.get("/walls/{wall_id}", response_model=dict)
async def get_wall(wall_id: str):
    wall = db.walls.find_one({"_id": ObjectId(wall_id)})
    if not wall:
        raise HTTPException(status_code=404, detail="Wall not found")
    # Optional: Convert ObjectId to string for client response
    wall["id"] = str(wall["_id"])
    return wall
