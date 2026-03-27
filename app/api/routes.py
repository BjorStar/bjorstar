from fastapi import APIRouter, Request

router = APIRouter()

def get_client_ip(request: Request) -> str:
    xff = request.headers.get("X-Forwarded-For")
    if xff:
        return xff.split(",")[0].strip()

    xri = request.headers.get("X-Real-IP")
    if xri:
        return xri

    return request.client.host

@router.get("/ip")
async def read_ip(request: Request):
    return {"client_ip": get_client_ip(request)}
