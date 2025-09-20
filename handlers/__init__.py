from aiogram import  Router
from .commands import router as start_router
from .callbacks import router as callbacks_router

router = Router()

router.include_routers(start_router, callbacks_router)