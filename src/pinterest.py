import base64
import dotenv
import os

# Load environment variables before importing pinterest modules
dotenv.load_dotenv(".env.local")

from pinterest.organic.pins import Pin  # noqa: E402
from pinterest.organic.boards import Board  # noqa: E402
from pinterest.client import PinterestSDKClient  # noqa: E402

ACCESS_TOKEN = os.getenv("PINTEREST_ACCESS_TOKEN")


class PinterestClient:
    def __init__(self):
        self.client = PinterestSDKClient.create_client_with_token(
            access_token=ACCESS_TOKEN
        )

    def get_or_create_board(self, name: str):
        boards = Board.get_all(client=self.client)
        if not boards:
            return Board.create(name=name, client=self.client)
        return boards[0]

    def create_pin(
        self,
        board_id: str,
        png_image_bytes: bytes,
        title: str,
        description: str,
        link: str,
        alt_text: str,
    ):
        pin = Pin.create(
            board_id=board_id,
            media_source={
                "source_type": "image_base64",
                "content_type": "image/png",
                "data": base64.b64encode(png_image_bytes).decode("utf-8"),
            },
            title=title,
            description=description,
            link=link,
            alt_text=alt_text,
            client=self.client,
        )
        return pin


# Initialize client
# client = PinterestSDKClient.create_client_with_token(access_token=ACCESS_TOKEN)

# boards = Board.get_all(client=client)[0]
# if not boards:
#     board = Board.create(name="Starfield Worldspeak Test", client=client)
# else:
#     board = boards[0]

# Generate image
# image = generate_image("Communicate over the phone with anyone in any language")
# save_generated_image(image, "worldspeak.png")
# image_bytes = get_image_bytes(image)
# image_bytes = get_bytes_from_local_image("worldspeak.png")

# Create a pin
# pin = Pin.create(
#     board_id=board.id,
#     media_source={
#         "source_type": "image_base64",
#         "content_type": "image/png",
#         "data": base64.b64encode(image_bytes).decode("utf-8"),
#     },
#     title="Starfield Worldspeak",
#     description="Communicate over the phone with anyone in any language",
#     link="https://worldspeak.starfield.app",
#     alt_text="Communicate over the phone with anyone in any language",
#     client=client,
# )

# print(f"Created pin with ID: {pin.id}")
