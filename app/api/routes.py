from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/ip")
async def read_ip(request: Request):
    return {"client_ip": request.client.host}
