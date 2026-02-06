from .posts import router as posts_router
from .tag import router as tag_router
from .category import router as category_router
from .weather import router as weather_router
from .users import router as users_router
from .auth import router as auth_router
from .lesson import router as lesson_router

__all__ = [
    "posts_router",
    "tag_router",
    "category_router",
    "profession_router",
    "weather_router",
    "users_router",
    "auth_router",
    "lesson_router"
]