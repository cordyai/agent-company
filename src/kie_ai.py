import requests
import os
import dotenv
import dataclasses
from collections.abc import Sequence
import json

dotenv.load_dotenv(".env.local")

KIE_AI_API_KEY = os.getenv("KIE_AI_API_KEY")
CREATE_TASK_URL = "https://api.kie.ai/api/v1/jobs/createTask"
AUTHORIZATION_HEADER = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {KIE_AI_API_KEY}",
}


@dataclasses.dataclass(frozen=True)
class Scene:
    description: str
    duration: float

    def to_dict(self):
        return {"Scene": self.description, "duration": self.duration}


def generate_storyboard(scenes: Sequence[Scene]) -> str:
    VALID_DURATIONS = [10.0, 15.0, 25.0]
    if sum(scene.duration for scene in scenes) not in VALID_DURATIONS:
        raise ValueError(f"Invalid duration: {sum(scene.duration for scene in scenes)}")

    payload = {
        "model": "sora-2-pro-storyboard",
        "input": {
            "n_frames": str(int(sum(scene.duration for scene in scenes))),
            "aspect_ratio": "portrait",
            "shots": [scene.to_dict() for scene in scenes],
        },
    }

    response = requests.post(
        CREATE_TASK_URL, headers=AUTHORIZATION_HEADER, json=json.dumps(payload)
    )
    result = response.json()
    print(result)
    if result["code"] != 200:
        raise ValueError(f"Failed to generate storyboard: {result['msg']}")
    return result["data"]["taskId"]


if __name__ == "__main__":
    scenes = [
        Scene(
            description="A cute fluffy green-leafed animated character, resembling a friendly leafy sprite, emerges from a lush sustainable garden, playfully gathering fresh organic vegetables into an eco-friendly basket labeled 'Leafy Larder', sunlight filtering through leaves, cinematic wide shot panning smoothly, vibrant colors, uplifting and eco-conscious atmosphere.",
            duration=5.0,
        ),
        Scene(
            description="The same cute fluffy leafy sprite now in a cozy modern kitchen, happily unpacking the basket to reveal sustainable packaging and vibrant produce, with a gentle smile and text overlay 'Shop Sustainable at LeafyLarder.com', warm soft lighting, cinematic close-up, shallow depth of field, inspiring mood to drive immediate action.",
            duration=5.0,
        ),
    ]
    task_id = generate_storyboard(scenes)
