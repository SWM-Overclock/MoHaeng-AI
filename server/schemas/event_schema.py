# make two serializers for event and event list

# event serializer
def event_serializer(event):
    return {
        "_id": str(event["_id"]),
        "code": event["code"],
        "name": event["name"],
        "price": event["price"],
        "type": event["type"],
        "image": event["image"],
        "category": event["category"]
    }


# event list serializer
def events_serializer(events):
    return [event_serializer(event) for event in events]