from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<html><body><b>This is ESP32 server</b></body></html>"

# endpoint /motor/forward to send GET request to ip address of ESP32
@app.get("/forward")
async def forward():
    url = "http://tumbller/motor/forward"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text

# endpoint /motor/forward to send GET request to ip address of ESP32
@app.get("/back")
async def forward():
    url = "http://tumbller/motor/back"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text