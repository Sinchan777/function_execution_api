import os
from utils.logger import log_execution

#code template as given in the assignment
CODE_TEMPLATE = 
"""
from automation.{module} import {function}

def main():
    try:
        {function}()
        print("{function} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
"""
#function to generate code for a given module and function in the specified tempalte
def generate_code(module, function, output_file="generated_script.py"):
    try:
        code = CODE_TEMPLATE.format(module=module, function=function)
        
        with open(output_file, "w") as file:
            file.write(code)
        
        log_execution("generate_code", "SUCCESS", f"Generated code for {function} in {output_file}")
        return {"status": "success", "file": output_file}
    except Exception as e:
        log_execution("generate_code", "ERROR", str(e))
        return {"status": "error", "message": str(e)}
