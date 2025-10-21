from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip


def get_video_clip(video_path: str) -> VideoFileClip:
    return VideoFileClip(video_path)


def add_text_overlay(
    video_clip: VideoFileClip,
    text: str,
    fontsize: int = 24,
    color: str = "white",
    font: str = "Arial",
) -> CompositeVideoClip:
    text_clip = TextClip(txt=text, fontsize=fontsize, color=color, font=font)
    text_clip.set_position(("center", "center"))
    return CompositeVideoClip([video_clip, text_clip])


def add_music(video_clip: VideoFileClip, music_path: str) -> CompositeVideoClip:
    music_clip = AudioFileClip(music_path)
    return CompositeVideoClip([video_clip, music_clip])


if __name__ == "__main__":
    video_clip = get_video_clip("videos/A_heartfelt_14second_202510201939_2ecf1.mp4")
    video_clip = add_text_overlay(video_clip, "Hello, World!")
    video_clip.duration = 8.0
    video_clip.write_videofile("videos/video_with_text.mp4")
