from fastapi import APIRouter, FastAPI

from app.api.v1.routers import router as v1_router

app = FastAPI()

router = APIRouter(prefix="/api")
router.include_router(v1_router)
app.include_router(router=router)
