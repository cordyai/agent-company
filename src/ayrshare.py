"""Post to social media platforms using AYRSHARE API.

To support a new social media platform see:
https://www.ayrshare.com/docs/apis/post/post

You there need to implement the relevant options for the platform, for instance
pinterestOptions for Pinterest.
"""

import requests
import dotenv
import os

dotenv.load_dotenv(".env.local")

AYRSHARE_API_KEY = os.getenv("AYRSHARE_API_KEY")


def post(payload: dict):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AYRSHARE_API_KEY}",
    }
    r = requests.post(
        "https://api.ayrshare.com/api/post", json=payload, headers=headers
    )
    return r.json()


def pinterest_post(title: str, media_url: str, link: str):
    """Post to Pinterest using AYRSHARE API.

    Options: https://www.ayrshare.com/docs/apis/post/social-networks/pinterest#pinterest-options"""
    payload = {
        "post": title,
        "platforms": ["pinterest"],
        "mediaUrls": [
            media_url,
        ],
        "pinterestOptions": {
            "link": link,
        },
    }
    return post(payload)


if __name__ == "__main__":
    pinterest_post(
        title="Today is a great day!",
        description="Today is a great day!",
        image_url="https://res.cloudinary.com/dy6xqduxc/image/upload/v1760967322/worldspeak.png",
    )
