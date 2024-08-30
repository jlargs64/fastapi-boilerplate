from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.database import engine
from app.models import item
import uvicorn

item.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App with Relational DB")

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI app!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )