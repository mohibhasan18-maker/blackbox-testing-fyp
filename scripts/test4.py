import requests

API_URL = "http://127.0.0.1:8000/predict"

response = requests.post(API_URL, files={})  # No file

print("Use Case 4: No File Uploaded")
print("Status Code:", response.status_code)
print("Response:", response.text)
print("-" * 50)
