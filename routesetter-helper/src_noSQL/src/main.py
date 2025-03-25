from fastapi import FastAPI
from src_noSQL.src.core.api.routes import router as api_router
from src_noSQL.src.core.api.walls import router as walls_router
from src_noSQL.src.core.api.setter import router as setter_router

app = FastAPI(title="NoSQL Backend API")

# Include routers from different modules
app.include_router(api_router, prefix="/api")
app.include_router(walls_router, prefix="/api")
app.include_router(setter_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src_noSQL.src.main:app", host="0.0.0.0", port=8000, reload=True)
