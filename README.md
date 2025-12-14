"""
Black Box Testing - Skin Disease Detection API

This script performs four black-box tests on the FastAPI skin disease detection project.
It interacts with the API externally, without accessing internal code.

Use Cases:
1. Valid Image Prediction
2. Invalid File Upload
3. Large Image Upload
4. No File Uploaded
"""

import requests
import os

# -----------------------
# Config
# -----------------------
API_URL = "http://127.0.0.1:8000/predict"
TEST_IMAGES_DIR = "test_images"  # Folder with test images

# Ensure test_images folder exists
if not os.path.exists(TEST_IMAGES_DIR):
    os.makedirs(TEST_IMAGES_DIR)
    print(f"Create a folder named '{TEST_IMAGES_DIR}' and put test images inside it.")
    exit()

# -----------------------
# Helper function
# -----------------------
def run_test(description, file_path=None):
    files = {"file": open(file_path, "rb")} if file_path else {}
    try:
        response = requests.post(API_URL, files=files)
        status = response.status_code
        print(f"\n--- {description} ---")
        print("Status Code:", status)
        if status == 200:
            data = response.json()
            print("Predicted Class:", data["class"])
            print("Confidence:", data["confidence"])
            print("All Scores:", data["all_scores"])
        else:
            print("Response:", response.text)
    except Exception as e:
        print("Error:", e)
    finally:
        if file_path:
            files["file"].close()

# -----------------------
# Test Cases
# -----------------------

# 1️⃣ Valid Image Prediction
valid_image = os.path.join(TEST_IMAGES_DIR, "acne.jpg")
if os.path.exists(valid_image):
    run_test("Use Case 1: Valid Image Prediction", valid_image)
else:
    print(f"Place a valid image at {valid_image} for Use Case 1.")

# 2️⃣ Invalid File Upload
invalid_file = os.path.join(TEST_IMAGES_DIR, "not_an_image.txt")
if os.path.exists(invalid_file):
    run_test("Use Case 2: Invalid File Upload", invalid_file)
else:
    print(f"Place a non-image file at {invalid_file} for Use Case 2.")

# 3️⃣ Large Image Upload
large_image = os.path.join(TEST_IMAGES_DIR, "large_image.jpg")
if os.path.exists(large_image):
    run_test("Use Case 3: Large Image Upload", large_image)
else:
    print(f"Place a large image at {large_image} for Use Case 3.")

# 4️⃣ No File Uploaded
run_test("Use Case 4: No File Uploaded")
