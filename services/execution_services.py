from core.function_registry import get_function_by_name
from utils.logger import log_execution

def execute_function(function_name, *args, **kwargs):
    function = get_function_by_name(function_name)
    
    if function:
        try:
            result = function(*args, **kwargs)
            log_execution(function_name, "SUCCESS", f"Result: {result}")
            return {"status": "success", "result": result}
        except Exception as e:
            log_execution(function_name, "ERROR", str(e))
            return {"status": "error", "message": str(e)}
    
    return {"error": "Function not found"}
