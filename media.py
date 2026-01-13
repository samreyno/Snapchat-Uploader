import requests

SNAPCHAT_API_BASE = "https://adsapi.snapchat.com/v1"


class MediaUploader:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def upload_image(self, account_id: str, image_url: str):
        url = f"{SNAPCHAT_API_BASE}/accounts/{account_id}/media"
        payload = {
            "type": "IMAGE",
            "source_url": image_url
        }

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def upload_video(self, account_id: str, video_url: str):
        url = f"{SNAPCHAT_API_BASE}/accounts/{account_id}/media"
        payload = {
            "type": "VIDEO",
            "source_url": video_url
        }

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()
