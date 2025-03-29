import webbrowser
from utils.logger import log_execution
def open_chrome():
    try:
        webbrowser.open("https://www.google.com")
        log_execution("open_chrome", "SUCCESS")
    except Exception as e:
        log_execution("open_chrome", "ERROR", str(e))

def open_calculator():
    try:
        os.system("gnome-calculator") # Since I am on a linux machine
        log_execution("open_calculator", "SUCCESS")
    except Exception as e:
        log_execution("open_calculator", "ERROR", str(e))

def open_notepad():
    try:
        os.system("gedit")  # Windows Only
        log_execution("open_notepad", "SUCCESS")
    except Exception as e:
        log_execution("open_notepad", "ERROR", str(e))

def open_spotify():
    try:
        webbrowser.open("https://open.spotify.com")
        log_execution("open_spotify", "SUCCESS")
    except Exception as e:
        log_execution("open_spotify", "ERROR", str(e))

def open_yt():
    try:
        webbrowser.open("https://www.youtube.com")
        log_execution("open_yt", "SUCCESS")
    except Exception as e:
        log_execution("open_yt", "ERROR", str(e))