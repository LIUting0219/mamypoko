# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request, session, url_for, redirect, render_template, json

# Flask 模块对象
module = Blueprint('main', __name__)

@module.route('/', methods=['GET'])
def index():
    return render_template('index.html', tab='index')

@module.route('/lobo/', methods=['GET'])
def lobo():
    return render_template('lobo.html')

@module.route('/520/', methods=['GET'])
def love():
    return render_template('520.html')

'''
@module.route('/introduce/', methods=['GET'])
def introduce():
	return render_template('introduce.html', tab='introduce')

@module.route('/news/', methods=['GET'])
def news():
	return render_template('news.html', tab='news')

@module.route('/product/', methods=['GET'])
def product():
	return render_template('product.html', tab='product')

@module.route('/contact/', methods=['GET'])
def contact():
	return render_template('contact.html', tab='contact')
'''