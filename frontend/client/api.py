from frontend.client.images import ImageClient
from frontend.config import config


class AppClient:

    def __init__(self, endpoint: str) -> None:
        self.images = ImageClient(endpoint)


appclient = AppClient(config.endpoint)
