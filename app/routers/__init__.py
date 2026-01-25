from .posts import router as posts_router
from .category import router as category_router
from .tag import router as tag_router

__all__ = [posts_router, category_router, tag_router]