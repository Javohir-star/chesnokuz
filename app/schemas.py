from datetime import datetime
from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    title: str
    body: str


class PostUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None


class PostListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CategoryCreateRequest(BaseModel):
    name: str | None = None


class CategoryUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None


class TagListResponse(BaseModel):
    id: int
    title: str
    slug: str
    body: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TagCreateRequest(BaseModel):
    name: str | None = None


class TagUpdateRequest(BaseModel):
    title: str | None = None
    body: str | None = None