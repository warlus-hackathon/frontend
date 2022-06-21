import logging

import httpx

from frontend.schemas import Image

logger = logging.getLogger(__name__)


class ImageClient:

    def __init__(self, url: str):
        self.url = f'{url}/images'

    def get_all(self) -> list[Image]:
        logger.debug(f'{self.url}/\n\n')
        res = httpx.get(f'{self.url}/')
        res.raise_for_status()
        images = res.json()
        return [Image(**image) for image in images]

    def get_by_id(self, image_id: int) -> Image:
        res = httpx.get(f'{self.url}/{image_id}')
        res.raise_for_status()
        image = Image(**res.json())
        return image

    def delete(self, image_id: int) -> None:
        res = httpx.delete(f'{self.url}/{image_id}')
        res.raise_for_status()
