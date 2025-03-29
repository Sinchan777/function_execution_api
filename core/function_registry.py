from automation.application_control import *
from automation.command_execution import *
from automation.file_operations import *
from automation.system_monitoring import *
from utils.logger import log_execution

FUNCTION_REGISTRY = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "open_notepad": open_notepad,
    "open_spotify": open_spotify,
    "open_yt": open_yt,
    "get_cpu_usage": get_cpu_usage,
    "get_ram_usage": get_ram_usage,
    "execute_command": execute_command,
    "create_file": create_file,
    "delete_file": delete_file,
    "move_file": move_file,
}

# Helper function to get function by name
def get_function_by_name(function_name):
    function = FUNCTION_REGISTRY.get(function_name)
    if function:
        log_execution("get_function_by_name", "SUCCESS", f"Retrieved function: {function_name}")
    else:
        log_execution("get_function_by_name", "ERROR", f"Function not found: {function_name}")
    return function
