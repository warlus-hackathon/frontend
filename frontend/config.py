import os

from pydantic import BaseModel


class WebAppConfig(BaseModel):
    port: str
    host: str
    loglevel: str


class AwsConfig(BaseModel):
    endpoint: str
    key_id: str
    key: str
    bucket_input_images: str
    bucket_output_images: str
    bucket_output_cvs: str


class AppConfig(BaseModel):
    endpoint: str
    aws: AwsConfig
    web: WebAppConfig


def load_from_env() -> AppConfig:
    endpoint = os.environ['ENDPOINT']
    app_port = os.environ['APP_PORT']
    app_host = os.environ['APP_HOST']
    app_loglevel = os.environ.get('APP_LOGLEVEL', 'INFO').upper()
    aws_endpoint = os.environ['AWS_ENDPOINT']
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    aws_bucket_input_images = os.environ['AWS_BUCKET_NAME_INPUT_IMAGES']
    aws_bucket_output_images = os.environ['AWS_BUCKET_NAME_OUTPUT_IMAGES']
    aws_bucket_output_cvs = os.environ['AWS_BUCKET_NAME_OUTPUT_CVS']
    return AppConfig(
        endpoint=endpoint,
        aws=AwsConfig(
            endpoint=aws_endpoint,
            key_id=aws_access_key_id,
            key=aws_secret_access_key,
            bucket_input_images=aws_bucket_input_images,
            bucket_output_images=aws_bucket_output_images,
            bucket_output_cvs=aws_bucket_output_cvs,
        ),
        web=WebAppConfig(port=app_port, host=app_host, loglevel=app_loglevel)
    )


config = load_from_env()
