from pathlib import Path

from frontend.aws import s3
from frontend.config import config


class CloudClient:

    def download_input_by_name(self, filename: str) -> None:
        upload_dir = Path('file_storage')
        upload_dir.mkdir(exist_ok=True, parents=True)
        s3.download_file(config.aws.bucket_input_images, filename, f'file_storage/{filename}')

    def download_output_by_name(self, filename: str) -> None:
        upload_dir = Path('file_storage')
        upload_dir.mkdir(exist_ok=True, parents=True)
        s3.download_file(config.aws.bucket_input_images, filename, f'file_storage/{filename}')
