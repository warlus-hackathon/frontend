from flask import Blueprint, render_template, redirect, url_for

from frontend.client.api import appclient

view = Blueprint('images', __name__)


@view.route('/')
def images():
    all_images = appclient.images.get_all()
    images = [image.dict() for image in all_images]
    for image in images:
        if image['was_recognized'] == 0:
            image['result_description'] = 'Распознавание не выполнялось'
        elif image['was_recognized'] == 1:
            image['result_description'] = 'Обнаружено объектов: {obj_number}'.format(
                obj_number=image['obj_number'])
        else:
            image['result_description'] = 'При распознавании произошла ошибка'
    return render_template(
        'images.html',
        images=images,
    )


@view.route('/delete/<int:image_uid>/')
def delete(image_uid):
    appclient.images.delete(image_uid)
    return redirect(url_for('images.images'))


@view.route('/result/<int:image_uid>/')
def result(image_uid):
    image = appclient.images.get_by_id(image_uid).dict()
    if image['was_recognized'] == 0:
        image['result_description'] = 'Распознавание не выполнялось'
    elif image['was_recognized'] == 1:
        image['result_description'] = 'Обнаружено объектов: {obj_number}'.format(
            obj_number=image['obj_number']
        )
    else:
        image['result_description'] = 'При распознавании произошла ошибка'
    filename = image['name'].split('.')[0]
    output_filename = f'{filename}_yolov3.jpg'
    appclient.cloud.download_output_by_name(output_filename)
    image_path = f'/../static/images/{output_filename}'
    return render_template('result.html',
                           image=image,
                           path=image_path
                           )
