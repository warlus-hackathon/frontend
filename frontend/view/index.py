from flask import Blueprint, render_template, redirect, url_for
from frontend.forms.upload import UploadFileForm

view = Blueprint('index', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    form = UploadFileForm(meta={'csrf': False})

    if form.validate_on_submit():
        form.upload_file()
        return redirect(url_for('index.index'))

    return render_template('index.html', form=form)
