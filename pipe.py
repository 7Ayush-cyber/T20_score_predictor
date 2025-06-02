# import requests
# import pickle

# url = "https://drive.google.com/uc?export=download&id=13Mfl3masRADZCGgNZypldghLLe8p5Qzm"

# print("Starting download...")
# response = requests.get(url)

# if response.status_code == 200:
#     with open("pipe.pkl", "wb") as f:
#         f.write(response.content)
#     print("Download complete. File saved as pipe.pkl")
# else:
#     print(f"Download failed with status code {response.status_code}")
#     exit()

# print("Loading the pickle file...")
# with open("pipe.pkl", "rb") as f:
#     pipe = pickle.load(f)

# print("Model pipeline loaded successfully.")
# pipe.py
import requests
import pickle
import os

def load_pipe():
    url = "https://drive.google.com/uc?export=download&id=13Mfl3masRADZCGgNZypldghLLe8p5Qzm"
    if not os.path.exists("pipe.pkl"):
        print("Starting download...")
        response = requests.get(url)
        if response.status_code == 200:
            with open("pipe.pkl", "wb") as f:
                f.write(response.content)
            print("Download complete. File saved as pipe.pkl")
        else:
            raise Exception(f"Download failed with status code {response.status_code}")
    print("Loading the pickle file...")
    with open("pipe.pkl", "rb") as f:
        pipe = pickle.load(f)
    return pipe
