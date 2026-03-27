from fastapi import FastAPI, Request
from api.ip import router as ip_router

app = FastAPI()

# This loads /api/ip from your router file
app.include_router(ip_router, prefix="/api")








