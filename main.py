from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.routes import router as auth_router
from app.api.upload.routes import router as upload_router
from app.api.dashboard.routes import router as dashboard_router
from app.api.ai.routes import router as ai_router
from app.api.forecast.routes import router as forecast_router
from app.api.reports.routes import router as reports_router
from app.api.health.routes import router as health_router

app = FastAPI(
    title="AI CFO API",
    version="1.0.0",
    description="Backend API for AI CFO"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(dashboard_router)
app.include_router(ai_router)
app.include_router(forecast_router)
app.include_router(reports_router)
app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": "AI CFO API Running"
    }
