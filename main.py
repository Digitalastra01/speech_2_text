from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import socketio
from transcribe import transcribe_audio

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Socket.IO
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def index(request: Request):
    port = request.url.port or 8000
    return templates.TemplateResponse("index.html", {"request": request, "port": port})

@sio.on('connect')
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.on('disconnect')
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.on('audio_chunk')
async def handle_audio_chunk(sid, data):
    print(f"Received audio_chunk from {sid}")
    try:
        audio_data = data['audio_data']  # Get binary audio data
        print(f"Audio data size: {len(audio_data)} bytes")
        
        # Run transcription in a separate thread to avoid blocking the async event loop
        # Since transcribe_audio is synchronous (uses torchaudio/groq sync client)
        import asyncio
        loop = asyncio.get_event_loop()
        print("Starting transcription...")
        transcription = await loop.run_in_executor(None, transcribe_audio, audio_data)
        
        print(f"Transcription result: {transcription}")

        # Emit transcription back to the client
        await sio.emit('transcription', {'text': transcription}, room=sid)
        print("Emitted transcription to client")
    except Exception as e:
        print(f"Error in handle_audio_chunk: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser(description="Run the Speech-to-Text Server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    args = parser.parse_args()

    print(f"\nStarting server...")
    print(f"Please access the application at: http://localhost:{args.port}")
    print(f"DO NOT use 0.0.0.0 or the IP address directly, as it blocks microphone access.\n")

    uvicorn.run(socket_app, host=args.host, port=args.port)