# src/core/api/setter.py
from fastapi import APIRouter, HTTPException
from src_noSQL.src.utils.database import db
from src_noSQL.src.schema.schema import WallUpdate
from bson.objectid import ObjectId

router = APIRouter()

@router.put("/wall/{wall_id}", response_model=dict)
async def set_wall_property(wall_id: str, update: WallUpdate):
    update_data = update.dict(exclude_unset=True)
    result = db.walls.update_one({"_id": ObjectId(wall_id)}, {"$set": update_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Wall not found or not updated")
    return {"updated": result.modified_count}
