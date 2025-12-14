import requests

API_URL = "http://127.0.0.1:8000/predict"
IMAGE_PATH = "test_images/acne.jpg"  # Example valid image

with open(IMAGE_PATH, "rb") as f:
    files = {"file": f}
    response = requests.post(API_URL, files=files)

assert response.status_code == 200, f"Expected 200, got {response.status_code}"

data = response.json()
print("Use Case 1: Valid Image Prediction")
print("Predicted Class:", data["class"])
print("Confidence:", data["confidence"])
print("All Scores:", data["all_scores"])
print("-" * 50)
