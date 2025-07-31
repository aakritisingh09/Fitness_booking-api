from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassBase(BaseModel):
    name: str
    instructor: str
    datetime: datetime
    total_slots: int

class ClassOut(ClassBase):
    id: int
    available_slots: int

    class Config:
        from_attributes = True  

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        from_attributes = True  

