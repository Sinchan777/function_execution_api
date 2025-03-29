import subprocess
from utils import log_execution

#function to execute shell commands
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        log_execution("execute_command", "SUCCESS", output)
        return output
    except Exception as e:
        log_execution("execute_command", "ERROR", str(e))
        return f"Error executing command: {str(e)}"