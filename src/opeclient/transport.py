import requests


class Transport:
    def __init__(self, base_url, project, token=None):
        self.base_url = base_url
        self.project = project
        self.token = token

    def _headers(self):
        headers = {
            "project": self.project
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, path):
        res = requests.get(
            f"{self.base_url}{path}",
            headers=self._headers()
        )
        return self._handle(res)

    def post(self, path, data):
        res = requests.post(
            f"{self.base_url}{path}",
            json=data,
            headers=self._headers()
        )
        return self._handle(res)

    def _handle(self, response):
        if response.status_code >= 400:
            raise Exception(response.text)
        return response.json()