import uuid
import cloudinary
import cloudinary.uploader
import dotenv
import os

dotenv.load_dotenv(".env.local")

CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

# Configuration
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True,
)


def upload_image(image_bytes: bytes) -> str:
    """Upload an image to Cloudinary.

    Returns the public URL of the uploaded image.
    """
    public_id = str(uuid.uuid4())
    upload_result = cloudinary.uploader.upload(
        image_bytes,
        public_id=public_id,
    )
    return upload_result["url"]
