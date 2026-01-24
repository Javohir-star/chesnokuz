from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Post
from app.schemas import PostCreateRequest, PostUpdateRequest, PostListResponse


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
)


@router.get("/get/", response_model=PostListResponse)
def get_post(post_id: int, session: Session = Depends(get_db)):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi")

    return post

@router.post("/create/", response_model=PostListResponse)
def create_post(data: PostCreateRequest, session: Session = Depends(get_db)):
    post = Post(
        title=data.title,
        body=data.body,
        slug=data.title.lower().replace(" ", "-"),
        user_id=1,          # vaqtincha
        category_id=None,
        is_active=True
    )

    session.add(post)
    session.commit()
    session.refresh(post)

    return post

@router.put("/update/")
def update_post(post_id: int, data: PostCreateRequest, session: Session = Depends(get_db)):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi")

    post.title = data.title
    post.body = data.body

    session.commit()
    session.refresh(post)

    return post

@router.patch("/patch/")
def patch_post(post_id: int, data: PostUpdateRequest, session: Session = Depends(get_db)):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi")

    if data.title is not None:
        post.title = data.title

    if data.body is not None:
        post.body = data.body

    session.commit()
    session.refresh(post)

    return post

@router.delete("/delete/")
def delete_post(post_id: int, session: Session = Depends(get_db)):
    stmt = select(Post).where(Post.id == post_id)
    res = session.execute(stmt)
    post = res.scalars().first()

    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi")

    session.delete(post)
    session.commit()

    return {"detail": "Post o‘chirildi"}
