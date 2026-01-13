from snapchat_uploader.client import SnapchatClient
from snapchat_uploader.media import MediaUploader
from snapchat_uploader.config import (
    SNAPCHAT_ACCESS_TOKEN,
    SNAPCHAT_ACCOUNT_ID,
)


class SnapchatUploader:
    def __init__(self):
        self.client = SnapchatClient(SNAPCHAT_ACCESS_TOKEN)
        self.media = MediaUploader(SNAPCHAT_ACCESS_TOKEN)

    def post_text(self, text: str):
        return self.client.publish_text(
            SNAPCHAT_ACCOUNT_ID,
            text
        )

    def post_image(self, image_url: str, caption: str | None = None):
        result = self.media.upload_image(
            SNAPCHAT_ACCOUNT_ID,
            image_url
        )
        if caption:
            self.post_text(caption)
        return result

    def post_video(self, video_url: str, caption: str | None = None):
        result = self.media.upload_video(
            SNAPCHAT_ACCOUNT_ID,
            video_url
        )
        if caption:
            self.post_text(caption)
        return result
