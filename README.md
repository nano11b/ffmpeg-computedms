# FFmpeg ComputeDMS

FFmpeg ComputeDMS is a distributed media processing system designed to scale FFmpeg workloads across multiple worker nodes. It enables automated media conversion and processing by distributing jobs to worker clients and managing them through a centralized server and dashboard.

The project is intended for environments where high-volume media transcoding or batch processing is required, such as media pipelines, streaming infrastructure, or distributed compute clusters.

---

## Overview

ComputeDMS provides a simple architecture for distributing FFmpeg workloads:

1. Media files are submitted to a central API server.
2. Jobs are placed into a queue for processing.
3. Worker clients retrieve jobs from the queue.
4. Each worker processes the media using FFmpeg.
5. The processed output is returned and made available for download.

This allows multiple compute nodes to work in parallel, dramatically increasing throughput for media processing workloads.

---

## Features

- Distributed FFmpeg processing
- Horizontally scalable worker nodes
- Centralized job queue
- Web-based dashboard for monitoring jobs
- Docker-friendly deployment
- API-driven job submission
- Automatic result retrieval

---

## Architecture

+-------------+
| Dashboard UI |
+------+------+
|
v
+-------------+
| API Server |
+------+------+
|
v
+-------------+
| Job Queue |
+------+------+
|
v
+-----------------------+
| Worker Nodes (FFmpeg) |
+-----------------------+

Workers can be scaled horizontally to handle increasing workloads.

---

## Use Cases

- Distributed video transcoding
- Automated media conversion pipelines
- Streaming platform preprocessing
- Batch media encoding
- Media research and experimentation
- Distributed compute clusters

---

## Technologies Used

- Python
- FFmpeg
- FastAPI
- Redis
- Celery
- Docker
- HTML Dashboard UI

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/nano11b/ffmpeg-computedms.git
cd ffmpeg-computedms

docker compose up --build
docker compose up --scale worker=5
```

Find the interface at http://localhost:8000

Scaling Workers

To increase processing capacity, simply scale the worker service:

```bash
docker compose up --scale worker=5
```
Each worker will automatically start processing jobs from the queue.

---

## Future Improvements

- GPU accelerated FFmpeg workers
- Real-time job progress tracking
- Authentication and user accounts
- Cloud storage integration (S3 / MinIO)
- Kubernetes deployment support
- Advanced job scheduling and prioritization

---

## License

MIT License

---

## Contributing

Pull requests and suggestions are welcome.
If you find a bug or have an idea for improvement, feel free to open an issue.
