import psutil #library to retrieve system information
from utils.logger import log_execution

#function to retrieve cpu usage returns percentage
def get_cpu_usage():
    function_name = "get_cpu_usage"
    try:
        usage = psutil.cpu_percent(interval=1)
        log_execution(function_name, "SUCCESS", f"CPU Usage: {usage}%")
        return f"CPU Usage: {usage}%"
    except Exception as e:
        log_execution(function_name, "ERROR", str(e))
        return f"Error: {e}"

#function to retrieve ram usage returns percentage
def get_ram_usage():
    function_name = "get_ram_usage"
    try:
        usage = psutil.virtual_memory().percent
        log_execution(function_name, "SUCCESS", f"RAM Usage: {usage}%")
        return f"RAM Usage: {usage}%"
    except Exception as e:
        log_execution(function_name, "ERROR", str(e))
        return f"Error: {e}"
