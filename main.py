from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import xml.etree.ElementTree as ET

app = FastAPI()

@app.post("/webhook/incoming-call")
async def handle_call(request: Request):
    form = await request.form()
    from_number = form.get("From", "Unknown")

    # Respond with Exotel XML instructions
    response = ET.Element("Response")
    speak = ET.SubElement(response, "Say")
    speak.text = f"Hello! Welcome. I am your AI assistant. Please tell me how I can help you."

    xml_str = ET.tostring(response, encoding="unicode")
    return PlainTextResponse(content=xml_str, media_type="application/xml")
