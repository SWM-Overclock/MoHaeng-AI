from pydantic import BaseModel, Field


# Event model
# event have 4 fields : name, price, type, image(url), category
class Event(BaseModel):
    code: str = Field(...)
    name: str = Field(...)
    price: int = Field(...)
    type: str = Field(...)
    image: str = Field(...)
    category: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "code": "202309CSCU00001",
                "name": "롯데)빅팜60g",
                "price": 2000,
                "type": "1+1",
                "image": "https://tqklhszfkvzk6518638.cdn.ntruss.com/product/8801123205219.jpg",
                "category": "식품"
            }
        }