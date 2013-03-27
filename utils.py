#!/usr/bin/env python

import os
import time
import random
import Image


def generate_name():
    now = str(time.time()).replace('.', '')
    random_str = str(random.random()).replace('.', '')
    return now + random_str


def generate_small_version(image_path):
    im = Image.open(image_path)
    x, y = im.size
    new_im = im.resize((int(x * 0.1), int(y * 0.1)),Image.ANTIALIAS)
    new_path_list = image_path.split('/')
    new_path_list.insert(-1, 'small_version')
    new_path = '/'.join(new_path_list)
    new_im.save(new_path) 
    return new_path
    

def prepare_before_run():
    if not os.path.exists('static/uploads/small_version'):
        os.makedirs('static/uploads/small_version')


if __name__ == '__main__':
    generate_small_version('gopher.png')
