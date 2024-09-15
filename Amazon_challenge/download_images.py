import os
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Function to download and save images
def download_images(image_url, save_dir, file_name):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save(os.path.join(save_dir, file_name))
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download {file_name}: {str(e)}")

# Function to resize images
def resize_image(image_path, size=(224, 224)):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        img.save(image_path)
        print(f"Resized: {image_path}")
    except Exception as e:
        print(f"Failed to resize {image_path}: {str(e)}")

# Function to process images: download and resize
def process_images(csv_file, save_dir, size=(224, 224)):
    # Load the CSV file containing image URLs
    df = pd.read_csv(csv_file)
    
    # Create the directory if it does not exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Loop through the DataFrame and process each image
    for index, row in df.iterrows():
        image_url = row['image_link']
        file_name = f"image_{index}.jpg"
        image_path = os.path.join(save_dir, file_name)
        
        # Download and save the image
        download_images(image_url, save_dir, file_name)
        
        # Resize the downloaded image
        resize_image(image_path, size)

# Path to your single dataset CSV file
csv_file = 'dataset/your_dataset.csv'  # Replace with your actual CSV file path

# Directory to save images
image_dir = 'images/'  # Directory to save images

# Download, resize, and save images
print("Processing images...")
process_images(csv_file, image_dir, size=(224, 224))

print("All images processed successfully!")
