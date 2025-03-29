from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.rag import retrieve_function
from services.execution_services import execute_function
from utils.logger import log_execution

app = FastAPI()

class TaskRequest(BaseModel):
    prompt: str

@app.post("/execute")
def execute_task(request: TaskRequest):
    function_data = retrieve_function(request.prompt)

    if "error" in function_data:
        log_execution("retrieve_function", "ERROR", function_data["error"])
        raise HTTPException(status_code=400, detail=function_data["error"])

    function_name = function_data["function"]
    execution_result = execute_function(function_name)

    return {
        "function": function_name,
        "execution_result": execution_result
    }
