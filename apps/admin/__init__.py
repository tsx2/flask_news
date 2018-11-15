# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:19' 


from flask import Blueprint, redirect

backend = Blueprint("admin", __name__)

import apps.admin.views

@backend.route('/', methods = ("GET", ))
def admin_home():
	return redirect('/admin/index/')


