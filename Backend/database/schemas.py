from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class DreamFactorBase(BaseModel):
    tagName: str
    description: str


class DreamFactorCreate(DreamFactorBase):
    pass


class DreamFactor(DreamFactorBase):
    factor_id: int
    dream_id: int

    class Config:
        orm_mode = True


class DreamImageBase(BaseModel):
    url: str


class DreamImageCreate(DreamImageBase):
    pass


class DreamImage(DreamImageBase):
    image_id: int
    dream_id: int

    class Config:
        orm_mode = True


class DreamBase(BaseModel):
    dateTime: datetime
    title: str
    inputPrompt: str
    context: str


class DreamCreate(DreamBase):
    factors: List[DreamFactorCreate]
    images: List[DreamImageCreate]


class Dream(DreamBase):
    id: int
    factors: List[DreamFactor] = []
    images: List[DreamImage] = []

    class Config:
        orm_mode = True
