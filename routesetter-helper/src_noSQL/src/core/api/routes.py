# src/core/api/routes.py
from fastapi import APIRouter, HTTPException
from src_noSQL.src.utils.database import db
from src_noSQL.src.utils.CRUD import create_item, get_item, update_item, delete_item
from src_noSQL.src.schema.schema import Item, ItemUpdate

router = APIRouter()

@router.post("/routes", response_model=dict)
async def create_new_item(item: Item):
    item_data = item.dict()
    item_id = create_item(db, item_data)
    return {"id": item_id}

@router.get("/routes/{item_id}", response_model=dict)
async def read_item(item_id: str):
    item = get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/routes/{item_id}", response_model=dict)
async def update_existing_item(item_id: str, item_update: ItemUpdate):
    update_data = item_update.dict(exclude_unset=True)
    updated_count = update_item(db, item_id, update_data)
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Item not found or not updated")
    return {"updated": updated_count}

@router.delete("/routes/{item_id}", response_model=dict)
async def delete_existing_item(item_id: str):
    deleted_count = delete_item(db, item_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": deleted_count}
