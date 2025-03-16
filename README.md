# LangChain Search API

A FastAPI service that performs web searches and provides summarized results using LangChain and OpenAI's GPT model.

## Project Structure
```
langchain-search-api/
├── src/
│   └── main.py         # Main application code
├── .env                # Environment variables (private)
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Features

- Web search using DuckDuckGo
- AI-powered summarization using OpenAI's GPT-3.5
- Configurable summary length
- RESTful API interface

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
The `.env` file should contain your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Server

Start the server with:
```bash
cd src
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

### GET /
- Welcome message and basic information

### POST /search
- Performs web search and returns summarized results
- Request body:
```json
{
    "query": "Your search query here",
    "max_words": 150  // optional, defaults to 150
}
```
- Response:
```json
{
    "summary": "Summarized search results..."
}
```

## Example Usage

```python
import requests

response = requests.post(
    "http://localhost:8000/search",
    json={
        "query": "Latest developments in AI",
        "max_words": 100
    }
)

print(response.json())
``` 