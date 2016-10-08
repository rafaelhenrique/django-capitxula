import os
import random
from django.forms import CharField, CheckboxSelectMultiple, MultipleChoiceField

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CARS_IMAGE_PATH = os.path.join(BASE_PATH, 'images', 'cars')


class Captcha(MultipleChoiceField):
    widget = CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        super(Captcha, self).__init__(*args, **kwargs)
        image_filenames = os.listdir(CARS_IMAGE_PATH)
        random.shuffle(image_filenames)

        image_list = []
        for image in image_filenames:
            image_full_path = os.path.join(CARS_IMAGE_PATH, image)
            choice = (image_full_path, image_full_path)
            image_list.append(choice)

        self.choices = image_list
