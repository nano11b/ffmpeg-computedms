import os
import subprocess
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "media_tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)

@celery_app.task(bind=True)
def convert_media(self, input_path, output_format):
    output_path = f"{input_path}.{output_format}"

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path
