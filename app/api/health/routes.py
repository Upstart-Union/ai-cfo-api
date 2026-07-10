from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
async def health_check():
    return {
        "status": "healthy",
        "message": "AI CFO API is running"
    }