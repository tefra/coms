from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["index", "home"])
async def index() -> dict:
    return {"status": "hello"}
