from datetime import datetime
from pydantic import BaseModel, Field
import enum
from typing import Optional, List

class OrderStatus(enum.Enum):
    Accepted = "Accepted"
    Pending = "Pending"
    Rejected = "Rejected"
class OrderCreate(BaseModel):
    user_id: int
    product_name: str = Field(min_length=1)
    quantity: int = Field(default=0, ge=0)
    total_price: float = Field(default=0.0, ge=0.0)
    order_date: datetime = Field(default_factory=datetime.now)
    order_status: OrderStatus
    order_notes: Optional[str] = Field(default=None, max_length=100)

class OrderGet(BaseModel):
    id: int
    user_id: int
    product_name: str = Field(min_length=1)
    quantity: int = Field(default=0, ge=0)
    total_price: float = Field(default=0.0, ge=0.0)
    order_date: datetime
    order_status: OrderStatus
    order_notes: Optional[str] = Field(default=None, max_length=100)