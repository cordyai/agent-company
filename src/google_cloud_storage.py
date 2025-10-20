import datetime
import dotenv
import os
from google.cloud import storage

dotenv.load_dotenv(".env.local")

GC_PROJECT_ID = os.getenv("GC_PROJECT_ID")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")


class GoogleCloudStorageClient:
    def __init__(self):
        self.client = storage.Client(project=GC_PROJECT_ID)
        self.bucket = self.client.bucket(GCS_BUCKET_NAME)

    def upload_public_image(self, image_bytes: bytes, filename: str) -> str:
        blob = self.bucket.blob(f"social-media/{filename}")
        blob.upload_from_string(image_bytes, content_type="image/png")
        # TODO: We should have a forever public url
        return blob.generate_signed_url(expiration=datetime.timedelta(days=180))


if __name__ == "__main__":
    client = GoogleCloudStorageClient()
    image_bytes = open("images/worldspeak.png", "rb").read()
    public_url = client.upload_public_image(image_bytes, "worldspeak.png")
    print(f"Image uploaded to {public_url}")
