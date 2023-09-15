from fastapi import APIRouter, HTTPException
from server.models.event_model import Event
from server.schemas.event_schema import event_serializer, events_serializer
from server.config.database import event_collection

event_router = APIRouter()

@event_router.post("/")
async def create_event(event: Event):
    event = dict(event)
    event_id = event_collection.insert_one(event)
    new_event = event_collection.find_one({"_id": event_id.inserted_id})
    return {"status": "Ok","data": event_serializer(new_event)}

@event_router.get("/")
async def find_all_events():
    events = events_serializer(event_collection.find())
    return {"status": "Ok","data": events}

@event_router.get("/{code}")
async def find_event(code):
    if (event := event_collection.find_one({"code": code})) is not None:
        return {"status": "Ok","data": event_serializer(event)}
    raise HTTPException(status_code=404, detail=f"Event {code} not found")

@event_router.put("/{code}")
async def update_event(code: str, event: Event):
    event_collection.find_one_and_update(
        {
            "code": code
        },
        {
            "$set": dict(event)
        })
    event = event_collection.find_one({"code": code})
    return {"status": "Ok","data": event_serializer(event)}

@event_router.delete("/{code}")
async def delete_event(code: str):
    event_collection.find_one_and_delete({"code": code})
    return {"status": "Ok","data": f"Event {code} deleted"}

