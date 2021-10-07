import random
import string
from django.template.defaultfilters import slugify
from django.utils.html import format_html


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str


def admin_img(img):
    return format_html(f'<img style="border-radius: 10px;margin-left:20px;" src="{img}" height="40" />')


def auto_slug(model, title, slug):
    if slug:
        slug = slug
    else:
        slug = slugify(title)
        if model.objects.filter(slug=slug).exists():
            while True:
                if not model.objects.filter(slug=slug).exists():
                    break
                slug = slug + '-' + get_random_string(1)
    return slug
