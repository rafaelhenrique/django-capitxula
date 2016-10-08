import os
import random
from django.forms import CharField, CheckboxSelectMultiple, MultipleChoiceField

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CARS_IMAGE_PATH = os.path.join(BASE_PATH, 'images', 'cars')


class Captcha(MultipleChoiceField):
    image_filenames = os.listdir(CARS_IMAGE_PATH)
    widget = CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        super(Captcha, self).__init__(*args, **kwargs)
        self.choices = (
            ("a", "A"),
            ("b", "B"),
        )
        print(BASE_PATH)
        print(CARS_IMAGE_PATH)
        # image = random.choice(self.image_filenames)
        # image_path = os.path.join(CARS_IMAGE_PATH, image)
        # self.label = image_path
