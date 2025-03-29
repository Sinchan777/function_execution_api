import requests

API_URL = "http://127.0.0.1:8000/execute"

def test_execution(prompt):
    response = requests.post(API_URL, json={"prompt": prompt})
    print(f"Prompt: {prompt}")
    print("Response:", response.json())

if __name__ == "__main__":
    test_execution("give ram usage") ### This is the prompt to be sent to the API