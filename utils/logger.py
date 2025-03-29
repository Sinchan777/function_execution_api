import logging

#logger configuration
logging.basicConfig(
    filename = "logs/automation.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

#a custom logger
def log_execution(function_name, status, message=""):
    logging.info(f"Function: {function_name} | Status: {status} | Message: {message}")