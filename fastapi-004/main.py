from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()

# Mount the static directory to serve images
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple OG Tags Example</title>
        <!-- Open Graph meta tags -->
        <meta property="og:title" content="Simple OG Tags Example">
        <meta property="og:type" content="website">
        <meta property="og:url" content="http://localhost/">
        <meta property="og:image" content="http://localhost/whatIsMyPurpose.jpg">
        <meta property="og:description" content="A simple example of Open Graph meta tags.">
        <meta property="og:site_name" content="Simple OG Tags Site">
        <!-- Farcaster frame meta tags -->
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="http://localhost/static/whatIsMyPurpose.jpg">
        <meta property="fc:frame:button1" content="Button 1">
        <meta property="fc:frame:button1:action" content="http://localhost/forward">

        <meta property="fc:frame:button2" content="Button 2">
        <meta property="fc:frame:button2:action" content="http://localhost/back">

        <meta property="fc:frame:button3" content="Button 3">
        <meta property="fc:frame:button3:action" content="http://localhost/stop">

    </head>
    <body>
        <h1>Tumbller Farcaster Frame Server</h1>
        <p>This will run commands on Tumbller</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# endpoint /motor/forward to send GET request to ip address of ESP32
@app.post("/forward")
async def forward():
    url = "http://tumbller/motor/forward"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple OG Tags Example</title>
        <!-- Open Graph meta tags -->
        <meta property="og:title" content="Simple OG Tags Example">
        <meta property="og:type" content="website">
        <meta property="og:url" content="http://localhost/">
        <meta property="og:image" content="http://localhost/movingForward.png">
        <meta property="og:description" content="A simple example of Open Graph meta tags.">
        <meta property="og:site_name" content="Simple OG Tags Site">
        <!-- Farcaster frame meta tags -->
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="http://localhost/movingForward.png">
        <meta property="fc:frame:button1" content="Button 1">
        <meta property="fc:frame:button1:action" content="http://localhost/forward">
        <meta property="fc:frame:button1:target" content="_blank">
        <meta property="fc:frame:button2" content="Button 2">
        <meta property="fc:frame:button2:action" content="http://localhost/back">
        <meta property="fc:frame:button2:target" content="_blank">
        <meta property="fc:frame:button3" content="Button 3">
        <meta property="fc:frame:button3:action" content="http://localhost/stop">
        <meta property="fc:frame:button3:target" content="_blank">
    </head>
    <body>
        <h1>Tumbller Farcaster Frame Server</h1>
        <p>This will run commands on Tumbller</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# endpoint /motor/back to send GET request to ip address of ESP32
@app.post("/back")
async def back():
    url = "http://tumbller/motor/back"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple OG Tags Example</title>
        <!-- Open Graph meta tags -->
        <meta property="og:title" content="Simple OG Tags Example">
        <meta property="og:type" content="website">
        <meta property="og:url" content="http://localhost/">
        <meta property="og:image" content="http://localhost/movingBack.png">
        <meta property="og:description" content="A simple example of Open Graph meta tags.">
        <meta property="og:site_name" content="Simple OG Tags Site">
        <!-- Farcaster frame meta tags -->
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="http://localhost/movingBack.png">
        <meta property="fc:frame:button1" content="Button 1">
        <meta property="fc:frame:button1:action" content="http://localhost/forward">
        <meta property="fc:frame:button1:target" content="_blank">
        <meta property="fc:frame:button2" content="Button 2">
        <meta property="fc:frame:button2:action" content="http://localhost/back">
        <meta property="fc:frame:button2:target" content="_blank">
        <meta property="fc:frame:button3" content="Button 3">
        <meta property="fc:frame:button3:action" content="http://localhost/stop">
        <meta property="fc:frame:button3:target" content="_blank">
    </head>
    <body>
        <h1>Tumbller Farcaster Frame Server</h1>
        <p>This will run commands on Tumbller</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


# endpoint /motor/stop to send GET request to ip address of ESP32
@app.post("/stop")
async def stop():
    url = "http://tumbller/motor/stop"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple OG Tags Example</title>
        <!-- Open Graph meta tags -->
        <meta property="og:title" content="Simple OG Tags Example">
        <meta property="og:type" content="website">
        <meta property="og:url" content="http://localhost/">
        <meta property="og:image" content="http://localhost/whatIsMyPurpose.jpg">
        <meta property="og:description" content="A simple example of Open Graph meta tags.">
        <meta property="og:site_name" content="Simple OG Tags Site">
        <!-- Farcaster frame meta tags -->
        <meta property="fc:frame" content="vNext" />
        <meta property="fc:frame:image" content="http://localhost/whatIsMyPurpose.jpg">
        <meta property="fc:frame:button1" content="Button 1">
        <meta property="fc:frame:button1:action" content="http://localhost/forward">
        <meta property="fc:frame:button2" content="Button 2">
        <meta property="fc:frame:button2:action" content="http://localhost/back">
        <meta property="fc:frame:button3" content="Button 3">
        <meta property="fc:frame:button3:action" content="http://localhost/">

    </head>
    <body>
        <h1>Tumbller Farcaster Frame Server</h1>
        <p>This will run commands on Tumbller</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
