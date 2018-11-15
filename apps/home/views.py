# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:20' 


from flask import Response, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash

from . import front

from functools import wraps

#登录装饰器
def check_user_login(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if "user" not in session:
			return redirect(url_for("home.home_login"))
		return func(*args, **kwargs)
	return decorated_function


'''
子模块的逻辑处理函数，都是注册到当前子模块蓝图上（通过子模块蓝图注册到app上，来统一的启动服务）
'''
@front.route('/index')
def index():
	'''
    前端新闻首页
    :return:
    '''
	from apps.models import News
	news_list = News.query.filter().order_by(News.created_at.desc())
	return render_template('home/index.html', news_list=news_list)



@front.route('/cat/<name>/')
def cat(name):
	'''
    新闻类别
    :param name:
    :return:
    '''
	#查询类别为name的新闻数据
	from apps.models import News
	news_list = News.query.filter(News.types == name)
	return render_template('home/cat.html', name=name, news_list=news_list)



@front.route('/detail/<int:pk>/')
def detail(pk):
	'''
    新闻详情信息
    :param pk:
    :return:
    '''
	from apps.models import News
	new_obj = News.query.get(pk)
	return render_template('home/detail.html', pk=pk, new_obj=new_obj)

