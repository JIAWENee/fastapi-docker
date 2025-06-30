from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="FastAPI Demo", version="1.0.0")

class NameRequest(BaseModel):
    name: str

class HelloResponse(BaseModel):
    message: str

@app.post("/hello", response_model=HelloResponse)
async def hello_name(request: NameRequest):
    """
    POST API 接口：接收 name 参数，返回 hello name
    """
    return HelloResponse(message=f"hello {request.name}")

@app.get("/")
async def root():
    """
    根路径，返回API信息
    """
    return {"message": "FastAPI Demo is running!"}

@app.get("/health")
async def health_check():
    """
    健康检查接口
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 