import httpx
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from werkzeug.utils import secure_filename

from frontend.config import config

upload_url = f'{config.endpoint}/upload/'


class UploadFileForm(FlaskForm):
    file = FileField(
        'File', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg'], 'Images only!')]
    )

    def upload_file(self) -> bool:
        file = self.file.data
        filename = secure_filename(file.filename)
        files = {'file': (filename, file)}
        timeout = httpx.Timeout(5.0, connect=5.0, read=50.0, write=5.0)
        answer = httpx.post(upload_url, files=files, timeout=timeout)

        if answer.status_code != '201':
            return False

        return True
