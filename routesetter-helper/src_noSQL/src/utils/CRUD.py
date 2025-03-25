# src/utils/CRUD.py
from bson.objectid import ObjectId

def create_item(db, data: dict) -> str:
    result = db.items.insert_one(data)
    return str(result.inserted_id)

def get_item(db, item_id: str) -> dict:
    try:
        item = db.items.find_one({"_id": ObjectId(item_id)})
        if item:
            # Convert the ObjectId to string for easier handling on the client side.
            item["id"] = str(item["_id"])
        return item
    except Exception:
        return None

def update_item(db, item_id: str, update_data: dict) -> int:
    result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": update_data})
    return result.modified_count

def delete_item(db, item_id: str) -> int:
    result = db.items.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count
