from pathlib import Path

from frontend.aws import s3
from frontend.config import config


class CloudClient:

    def download_input_by_name(self, filename: str) -> None:
        upload_dir = Path('frontend/static/images')
        upload_dir.mkdir(exist_ok=True, parents=True)
        s3.download_file(config.aws.bucket_input_images, filename, f'{upload_dir}/{filename}')

    def download_output_by_name(self, filename: str) -> None:
        upload_dir = Path('frontend/static/images')
        s3.download_file(config.aws.bucket_output_images, filename, f'{upload_dir}/{filename}')
