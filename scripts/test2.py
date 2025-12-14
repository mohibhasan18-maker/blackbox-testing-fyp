import requests

API_URL = "http://127.0.0.1:8000/predict"
INVALID_FILE_PATH = "test_images/not_an_image.txt"

with open(INVALID_FILE_PATH, "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)

print("Use Case 2: Invalid File Upload")
print("Status Code:", response.status_code)
print("Response:", response.text)
print("-" * 50)
