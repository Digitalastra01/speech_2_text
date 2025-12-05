# Real-time Speech-to-Text Web Application

A modern, real-time speech-to-text web application powered by **FastAPI**, **Socket.IO**, and **Groq's Whisper API**. It features a responsive, glassmorphism-inspired UI with an olive green theme.

## Features

-   **Real-time Transcription**: Streams audio from the browser to the backend for instant transcription using Groq's Whisper model.
-   **Modern UI**: Beautiful, dark-mode interface with an olive green color palette and glassmorphism effects.
-   **FastAPI Backend**: High-performance, asynchronous backend using FastAPI and Uvicorn.
-   **Secure Context Enforcement**: Ensures microphone access by enforcing `localhost` usage.
-   **Dynamic Port Configuration**: Run the server on any port via CLI arguments.

## Prerequisites

-   Python 3.10+
-   A [Groq API Key](https://console.groq.com/)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd speech_2_text
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install .
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your Groq API key:
    ```env
    GROQ_API_KEY='your_groq_api_key_here'
    ```

## Usage

1.  **Run the application:**
    ```bash
    python main.py
    ```
    *Optional: Specify a custom port:*
    ```bash
    python main.py --port 8001
    ```

2.  **Access the application:**
    Open your browser and navigate to:
    **[http://localhost:8000](http://localhost:8000)**

    > **Important:** You MUST use `localhost`. Accessing via `0.0.0.0` or an IP address will block microphone access due to browser security policies.

3.  **Start Recording:**
    -   Grant microphone permission when prompted.
    -   Click **"Start Recording"** to begin.
    -   Speak into your microphone, and the transcription will appear in real-time.

## Project Structure

-   `main.py`: Entry point. Sets up the FastAPI app, Socket.IO server, and serves static files.
-   `transcribe.py`: Handles audio file processing and interaction with the Groq API.
-   `templates/index.html`: Frontend HTML/JS with Socket.IO client and audio recording logic.
-   `static/style.css`: Custom CSS with olive green theme and glassmorphism styles.
-   `pyproject.toml`: Project configuration and dependencies.

## Tech Stack

-   **Backend**: FastAPI, Uvicorn, Python-SocketIO
-   **Frontend**: HTML5, CSS3, JavaScript, Socket.IO Client
-   **AI/ML**: Groq API (Whisper Large V3)
