from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import generate_response 

app = FastAPI(title="Movies Chatbot")

class QuestionRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: QuestionRequest):
    response = generate_response(request.question)
    if response:
        return {"answer": response}
    else:
        raise HTTPException(status_code=404, detail="Resposta não encontrada para a pergunta fornecida.")
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
