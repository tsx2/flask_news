# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:19' 

from flask import Blueprint

front = Blueprint("home", __name__)

import apps.home.views

