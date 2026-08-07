import opendatasets as od
import os

# This script downloads the 5000 images directly from Kaggle
dataset_url = "https://www.kaggle.com/datasets/andrewmvd/safety-helmet-detection"

print("Downloading dataset... (This requires your Kaggle API token)")
print("You can get your API token from: https://www.kaggle.com/settings -> Create New Token")

od.download(dataset_url, force=True)

# Rename the folder to 'input' to match the Kaggle structure
if os.path.exists("safety-helmet-detection"):
    os.rename("safety-helmet-detection", "input")
    print("Dataset downloaded successfully to the 'input' folder!")
