import requests
import hashlib
import os
from zipfile import ZipFile 
import shutil

urls = [
    "https://archive.ics.uci.edu/static/public/109/wine.zip"
]

expected_hashes = {
    "wine.zip": "2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab",
}

data_dir = "data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
else:
    shutil.rmtree(data_dir)
    os.makedirs(data_dir)

for url in urls:
    filename = url.split("/")[-1]
    file_path = os.path.join("data", filename)

    if os.path.exists(file_path):
        with open(file_path, mode='rb') as f:
            data = f.read()
            sha256hash = hashlib.sha256(data).hexdigest()
        if sha256hash != expected_hashes[filename]:
            print("Computed hash does not match expected hash")
        else:
            print("Computed hash matches expected hash")
    
    else:
        if ".zip" in filename:
            print(f"Downloading {filename}...")
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
            else:
                print(f"Error downloading {filename}. Status code: {response.status_code}")
                continue
            with open(file_path, mode='rb') as f:
                data = f.read()
                sha256hash = hashlib.sha256(data).hexdigest()
            if sha256hash != expected_hashes[filename]:
                print("Computed hash does not match expected hash")
            else:
                print("Computed hash matches expected hash")
                print("Verified file!")
                print("Extracting Zip File")
                with ZipFile("./data/wine.zip", 'r') as zip: 
                    zip.printdir() 
                    print('Extracting all files...') 
                    zip.extractall()
                    os.replace("Index", "./data/Index")
                    os.replace("wine.data", "./data/wine.data")
                    os.replace("wine.names", "./data/wine.names")
                    os.remove("./data/wine.zip")
                    print('Finished Extracting!') 