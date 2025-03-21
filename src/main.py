from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# Initialize FastAPI app
app = FastAPI(
    title="Search and Summarize API",
    description="A FastAPI service that performs web searches and summarizes results using LangChain",
    version="1.0.0"
)

# Initialize search tool and LLM
search = DuckDuckGoSearchRun()
llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize agent
agent = initialize_agent(
    tools=[search],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

class SearchRequest(BaseModel):
    query: str
    max_words: Optional[int] = 150

class SearchResponse(BaseModel):
    summary: str

@app.post("/search", response_model=SearchResponse)
async def search_and_summarize(request: SearchRequest):
    try:
        # Create the agent prompt
        prompt = f"""
        Search for information about: {request.query}
        
        After finding the information, provide a concise summary in no more than {request.max_words} words.
        Focus on the most important and relevant information.
        """
        
        # Run the agent
        result = agent.run(prompt)
        
        return SearchResponse(summary=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Search and Summarize API. Use /search endpoint to search and summarize content."}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 