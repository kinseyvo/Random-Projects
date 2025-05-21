from PIL import Image
import os

# Folder containing .webp images
input_folder = "./.../..."
output_folder = "./.../..."

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        webp_path = os.path.join(input_folder, filename)
        png_path = os.path.join(output_folder, filename.replace(".webp", ".png"))

        with Image.open(webp_path) as img:
            img.save(png_path, "PNG")
            print(f"Converted: {filename} -> {os.path.basename(png_path)}")
