import os
import shutil
import uuid
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from tasks import convert_media

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

jobs = {}

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "jobs": jobs}
    )

@app.post("/submit")
async def submit(file: UploadFile = File(...), output_format: str = Form(...)):
    job_id = str(uuid.uuid4())
    input_path = os.path.join(UPLOAD_DIR, job_id)

    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    task = convert_media.delay(input_path, output_format)

    jobs[job_id] = {
        "status": "processing",
        "task_id": task.id
    }

    return {"job_id": job_id}

@app.get("/status/{job_id}")
def status(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return {"error": "not found"}

    from tasks import celery_app
    result = celery_app.AsyncResult(job["task_id"])

    if result.ready():
        jobs[job_id]["status"] = "complete"
        jobs[job_id]["output"] = result.result

    return jobs[job_id]

@app.get("/download/{job_id}")
def download(job_id: str):
    job = jobs.get(job_id)
    if job and job.get("output"):
        return FileResponse(job["output"])
    return {"error": "not ready"}
