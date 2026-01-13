import requests

SNAPCHAT_API_BASE = "https://adsapi.snapchat.com/v1"


class SnapchatClient:
    def __init__(self, access_token: str):
        self.access_token = access_token

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def publish_text(self, account_id: str, text: str):
        url = f"{SNAPCHAT_API_BASE}/accounts/{account_id}/content"
        payload = {
            "type": "TEXT",
            "text": text
        }

        response = requests.post(url, json=payload, headers=self._headers())
        response.raise_for_status()
        return response.json()
