from pydantic import BaseModel
from typing import List, Optional

class HealthRecordBase(BaseModel):
    title: str
    description: str

class HealthRecordCreate(HealthRecordBase):
    pass

class HealthRecord(HealthRecordBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    health_records: List[HealthRecord] = []

    class Config:
        from_attributes = True
