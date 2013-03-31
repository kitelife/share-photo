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
    new_x, new_y = x, y
    if x > 550:
        new_x = 550
        rate = x / float(new_x)
        new_y = int(y / rate)
    new_im = im.resize((new_x, new_y),Image.ANTIALIAS)
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
