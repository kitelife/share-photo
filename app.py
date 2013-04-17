#!/usr/bin/env python
#coding: utf-8

from flask import Flask
from flask import request, redirect, url_for
from flask import render_template, send_file
from flask.ext.basicauth import BasicAuth
from utils import *
from db import Redis
import json
import os

app = Flask(__name__)
app.config['db'] = Redis()

app.config.from_pyfile('config.py')

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def index():
    photos = app.config['db'].get_all()
    #photos_num = len(photos)
    #right = [photos[index] for index in xrange(photos_num) if index % 2 == 1]
    #left = [photos[index] for index in xrange(photos_num) if index % 2 == 0]
    return render_template('index.html', site_title = app.config['SITE_TITLE'],
            photo_urls = json.dumps(photos))

@app.route('/upload', methods=['POST'])
def upload():
    for _, f in request.files.iteritems():
        suffix = f.filename.split('.')[-1]
        target_name = '{0}.{1}'.format(generate_name(), suffix)
        image_path = 'static/uploads/' + target_name
        f.save(image_path)
        small_image_path = generate_small_version(image_path)
        app.config['db'].set(image_path, small_image_path)
    return json.dumps({'success': True})

@app.route('/download', methods=['GET'])
def download():
    image_name = request.args.get('imgname', '')
    target_path = 'static/uploads/' + image_name
    if image_name and os.path.exists(target_path):
        image_type = image_name.split('.')[-1]
        mime_type = 'image/'+image_type
        return send_file(target_path, mimetype=mime_type, 
                as_attachment=True, attachment_filename=image_name)
    else:
        return "Not found that image"

@app.route('/delete', methods=['POST'])
def delete():
    image_name = request.form['imgname']
    target_path = 'static/uploads/' + image_name
    if image_name and os.path.exists(target_path):
        small_target_path = 'static/uploads/small_version/' + image_name
        try:
            os.remove(target_path)
            os.remove(small_target_path)
            app.config['db'].delete(target_path)
        except:
            print u"数据删除错误"
        return "OK"
    else:
        return "ERROR"
        
if __name__ == '__main__':
    prepare_before_run()
    app.run(debug=True)
