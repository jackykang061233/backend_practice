from pydantic import BaseModel, Field
import enum
from typing import Optional, List
from datetime import datetime

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(default=0.0, ge=0.0)
    description: str = Field(default=None, max_length=300)
    orders: Optional[List[int]] = []

    def get_created_time():
        return datetime.now()

    created_time: datetime = Field(default_factory=get_created_time)
    last_update: datetime = Field(default=None)

class ItemGet(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float = Field(default=0.0, ge=0.0)
    description: str = Field(default=None, max_length=300)
    orders: Optional[List[int]] = []

    created_time: datetime
    last_update: datetime = Field(default=None)
