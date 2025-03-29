def create_file(file_path):
    try:
        with open(file_path, 'w') as f:
            pass
        log_execution("create_file", "SUCCESS", f"Created {file_path}")
        return "File created"
    except Exception as e:
        log_execution("create_file", "ERROR", str(e))
        return f"Error creating file"

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            log_execution("delete_file", "SUCCESS", f"Deleted {file_path}")
            return "File deleted."
        log_execution("delete_file", "WARNING", f"File not found: {file_path}")
        return "File not found."
    except Exception as e:
        log_execution("delete_file", "ERROR", str(e))
        return f"Error deleting file"

def move_file(src, dest):
    try:
        shutil.move(src, dest)
        log_execution("move_file", "SUCCESS", f"Moved {src} to {dest}")
        return f"File moved to {dest}."
    except Exception as e:
        log_execution("move_file", "ERROR", str(e))
        return f"Error moving file"
