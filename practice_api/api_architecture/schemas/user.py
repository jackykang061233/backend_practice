from pydantic import BaseModel, Field, EmailStr
import enum
from typing import Optional, Union, List
from datetime import datetime

class UserSex(enum.Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"
class UserCreate(BaseModel):
    email: EmailStr
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    sex: Optional[UserSex] = Field(default=None)
    orders: Optional[List[str]] = []

    def get_created_time():
        return datetime.now()

    created_time: datetime = Field(default_factory=get_created_time)
    last_login: datetime = Field(default_factory=get_created_time)

class UserGet(BaseModel):
    id: int
    email: EmailStr
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    sex: Optional[UserSex] = Field(default=None)
    orders: Optional[List[str]] = []

    def get_created_time():
        return datetime.now()

    created_time: datetime
    last_login: datetime = Field(default_factory=datetime.now)