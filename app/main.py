import uvicorn
from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.database import get_db
from app.models import item

item.Base.metadata.create_all(bind=get_db())

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
