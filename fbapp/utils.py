import os
import random
import urllib.request as urllib
import io
from PIL import Image, ImageDraw, ImageOps, ImageFont
from fbapp.models import Content
from flask import url_for

def find_content(gender):
    contents = Content.query.filter(Content.gender == gender).all()
    ids = [content.id for content in contents]
    the_one = Content.query.get(random.choice(ids))
    return the_one

class OpenGraphImage:

    def __init__(self, first_name, profile_path, uid, description):
        self.location = self._location(uid)
        self.cover_location = self._cover_location(uid)

        background = self.base()
        img = self.to_img(profile_path)
        cropped = self.crop_image(img)
        cropped.resize((100, 100))
        cropped.save(self._path(uid, 'cover_'))
        # with_corners = self.add_corners(cropped)
        # air = background.paste(ok, (300, 100, ok.width+500, ok.height+100))
        self.print_on_img(background, first_name.capitalize(), 70, (450, 50))
        description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

        # Make sentences of 7 words from description
        sentence_length = 7
        words = description.split()
        for i in range(0, len(words), sentence_length):
            sentence = ' '.join(words[i:i+sentence_length])
            top = 200 + i*40/sentence_length
            left = 100
            self.print_on_img(background, sentence, 40, (left, top))

        background.save(self._path(uid))

    def _path(self, uid, pre=''):
        return os.path.join('fbapp', 'static', 'tmp', '{}{}.jpg'.format(pre, uid))

    def _location(self, uid):
        return url_for('static', filename='tmp/{}.jpg'.format(uid))

    def _cover_location(self, uid):
        return url_for('static', filename='tmp/cover_{}.jpg'.format(uid))

    def base(self):
        img = Image.new('RGB', (1200, 630), '#18BC9C')
        # img.save(self.path, 'JPEG')
        return img

    def to_img(self, path):
        fd = urllib.urlopen(path)
        image_file = io.BytesIO(fd.read())
        return Image.open(image_file)

    def crop_image(self, pic):
        size = min(pic.width, pic.height)
        left_margin = max(int((pic.width - pic.height)/2), 0)
        top_margin =  max(int((pic.height - pic.width)/2), 0)
        box = (left_margin, top_margin, size + left_margin, size + top_margin)
        return pic.crop(box)

    def print_on_img(self, img, text, size, position):
        font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts', 'Arcon-Regular.otf'), size)
        draw = ImageDraw.Draw(img)
        draw.text(position, text, (255, 255, 255), font=font)
        return img

    # Not working for the moment
    # def add_corners(self, image):
    #     size = (128, 128)
    #     mask = Image.new('L', size, 0)
    #     draw = ImageDraw.Draw(mask)
    #     draw.ellipse((0, 0) + size, fill=255)
    #     output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    #     return output.putalpha(mask)

        # im = image
        # bigsize = (im.size[0] * 3, im.size[1] * 3)
        # mask = Image.new("L", bigsize, 0)
        # draw = ImageDraw.Draw(mask)
        # draw.ellipse((0, 0) + bigsize, fill=255)
        # mask = mask.resize(im.size, Image.ANTIALIAS)
        # return im.putalpha(mask)
