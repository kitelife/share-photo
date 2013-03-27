#!/usr/bin/env python

import redis

class Redis(object):

    def __init__(self):
        self.server = redis.StrictRedis(host='localhost', port=6379, db=0)

    def set(self, key, value):
        self.server.set(key, value)

    def get(self, key):
        return self.server.get(key)

    def get_all(self):
        images = []
        for image in sorted(self.server.keys(), reverse=True):
            small_image = self.server.get(image)
            images.append({'origin': image, 'small': small_image})

        return images

if __name__ == '__main__':
    db = Redis()
    db.set('o', 'one')
    print db.get_all()
