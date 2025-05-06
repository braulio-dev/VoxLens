# VoxLens API

This is a FastAPI-based API service that provides speech recognition capabilities using the Whisper model.

## Building and Running with Docker

### Option 1: Using Docker Compose (Recommended)
```bash
# Start the service
docker compose up -d

# Stop the service
docker compose down
```

### Option 2: Using Docker directly
1. Build the Docker image:
```bash
docker build -t voxlens-api .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --gpus all voxlens-api
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /`: Welcome message
- `POST /transcribe`: Transcribe audio file
  - Accepts audio file upload
  - Returns JSON with transcribed text

## Example Usage

Using curl to transcribe an audio file:
```bash
curl -X POST "http://localhost:8000/transcribe" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/your/audio.wav"
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 