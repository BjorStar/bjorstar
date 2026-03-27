from fastapi import FastAPI

from app.api.routes import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return { "msg": "Hello!", "v": "0.1" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}





