from fastapi import FastAPI
from src.utils.database import engine, Base
from src.core.api.routes import router as routes_router
from src.core.api.walls import router as walls_router
from src.core.api.setter import router as setters_router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend's origin
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_router, prefix="/api/routes", tags=["routes"])
app.include_router(walls_router, prefix="/api/walls", tags=["walls"])
app.include_router(setters_router, prefix="/api/setters", tags=["setters"])


@app.get("/")
def read_root():
    return {"message": "Welcome, Route Setters!"}

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")