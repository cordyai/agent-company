import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import dotenv
import os

dotenv.load_dotenv(".env.local")

CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

# Configuration
cloudinary.config(
    cloud_name="dy6xqduxc",
    api_key="213115559217667",
    api_secret=CLOUDINARY_API_SECRET,  # Click 'View API Keys' above to copy your API secret
    secure=True,
)

image_bytes = open("images/worldspeak.png", "rb").read()

# Upload an image
upload_result = cloudinary.uploader.upload(
    image_bytes,
    public_id="worldspeak",
)
print(upload_result["secure_url"])
print(upload_result["url"])

# Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
# print(optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url(
#     "shoes", width=500, height=500, crop="auto", gravity="auto"
# )
# print(auto_crop_url)
