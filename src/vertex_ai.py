from google import genai
import dotenv
import os
import typing
import enum
from PIL import Image

dotenv.load_dotenv(".env.local")

VERTEX_AI_API_KEY = os.getenv("VERTEX_AI_API_KEY")


class AspectRatio(enum.Enum):
    _16_9 = "16:9"
    _9_16 = "9:16"
    _1_1 = "1:1"
    _4_3 = "4:3"
    _3_4 = "3:4"


class VertexAIClient:
    def __init__(self):
        self.client = genai.Client(api_key=VERTEX_AI_API_KEY)

    def generate_image(
        self, prompt: str, aspect_ratio: AspectRatio, enhance_prompt: bool = False
    ) -> genai.types.Image | None:
        generate_images_response = self.client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=genai.types.GenerateImagesConfig(
                aspect_ratio=aspect_ratio.value,
                number_of_images=1,
                image_size="2K",
                person_generation=genai.types.PersonGeneration.ALLOW_ADULT,
                enhance_prompt=enhance_prompt,
            ),
        )
        return generate_images_response.generated_images[0].image


# Save the generated image
def save_generated_image(
    image: genai.types.Image, filename: str, directory: str = "images"
):
    """Save the generated image to a file"""
    pil_image = typing.cast(Image.Image, image._pil_image)
    os.makedirs(directory, exist_ok=True)
    pil_image.save(os.path.join(directory, filename))
    print(f"Image saved as {filename}")


def get_image_bytes(image: genai.types.Image) -> bytes:
    """Get the image bytes from the image"""
    pil_image = typing.cast(Image.Image, image._pil_image)
    return pil_image.tobytes()


def get_bytes_from_local_image(
    filename: str, directory: str = "images"
) -> bytes | None:
    """Get the image bytes from a local image"""
    with open(os.path.join(directory, filename), "rb") as image_file:
        return image_file.read()
