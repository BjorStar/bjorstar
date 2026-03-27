from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/ip")
async def read_ip(request: Request):
    return {"client_ip": request.client.host}

