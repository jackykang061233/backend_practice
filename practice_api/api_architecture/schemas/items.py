from pydantic import BaseModel, Field
import enum
from typing import Optional, List
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    price: float
    description: str = Field(default=None, max_length=300)
    orders: Optional[List[str]] = []

    def get_created_time():
        return datetime.now()

    created_time: datetime = Field(default_factory=get_created_time)
    last_update: datetime = Field(default=None)

class ItemGet(BaseModel):
    id: str
    name: str
    price: float
    description: str = Field(ma_length=300)
    orders: Optional[List[str]] = []

    created_time: datetime
    last_update: datetime = Field(default=None)
