from .base import router as base_router
from .clientslist import router as clientlist_router
from .addclient import router as add_router
from .removeclient import router as remove_router

__all__ = ["base_router", "clientlist_router", "add_router", "remove_router"]
