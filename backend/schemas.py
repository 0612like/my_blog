from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True # Pydantic v1
        # from_attributes = True # Pydantic v2 