from flask import Blueprint, render_template

from frontend.client.api import appclient

view = Blueprint('images', __name__)


@view.route('/')
def images():
    all_images = appclient.images.get_all()
    images = [image.dict() for image in all_images]
    for image in images:
        if image['obj_number'] == -1:
            image['result_description'] = 'Распознавание не выполнено'
        else:
            image['result_description'] = 'На изображении обнаружено объектов:{obj_number}'.format(
                obj_number=image['obj_number']
            )
    return render_template(
        'images.html',
        images=images,
    )