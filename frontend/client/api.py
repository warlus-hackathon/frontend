import logging

from frontend.client.images import ImageClient
from frontend.client.cloud import CloudClient
from frontend.config import config

logger = logging.getLogger(__name__)


class AppClient:

    def __init__(self, endpoint: str) -> None:
        self.images = ImageClient(endpoint)
        self.cloud = CloudClient()


appclient = AppClient(config.endpoint)
