from fastapi import FastAPI
from api.ip import router as ip_router

app = FastAPI()


app.include_router(ip_router, prefix="/api")

@app.get("/api/ip")
async def read_ip(request: Request):
    return {"client_ip": request.client.host}








