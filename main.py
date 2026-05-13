from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import os

app = FastAPI(title="Jewel Hospital")

# Print current directory for debugging
print("Current directory:", os.getcwd())
print("Templates folder exists:", os.path.exists("templates"))

templates = Jinja2Templates(directory="templates")

appointments = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, success: str = None):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "hospital_name": "Jewel Hospital",
        "appointments": appointments,
        "success": success
    })


@app.post("/book-appointment")
async def book_appointment(
    name: str = Form(...),
    phone: str = Form(...),
    department: str = Form(...),
    date: str = Form(...),
    message: str = Form("")
):
    appointment = {
        "name": name,
        "phone": phone,
        "department": department,
        "date": date,
        "message": message,
        "booked_at": datetime.now().strftime("%d %b, %I:%M %p")
    }
    appointments.append(appointment)
    return RedirectResponse(url="/?success=1", status_code=303)
