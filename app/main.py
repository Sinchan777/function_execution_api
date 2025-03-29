import uvicorn
from api.api import app
from utils.logger import log_execution

#
if __name__ == "__main__":
    log_execution("server_start", "INFO", "Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)