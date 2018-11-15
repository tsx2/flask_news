# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:14' 

import os
from flask  import Flask, render_template, redirect, url_for

from apps.home import front  as home_blueprint
from apps.admin import backend  as admin_blueprint


#基于Flask创建的application
app = Flask(__name__)


#（1）注册各个模块子蓝图到app上
app.register_blueprint(home_blueprint, url_prefix="/home")
app.register_blueprint(admin_blueprint, url_prefix="/admin")

############ SQL Alchemy Settings start############
from flask_sqlalchemy import SQLAlchemy
mysql_conn_str = \
	"mysql+pymysql://zhougy:123456@192.168.51.81:3306/flask_news?charset=utf8"

#配置数据库连接，secret_key, 上传文件路径UP_DIR, 到app
app.config["SQLALCHEMY_DATABASE_URI"] = mysql_conn_str
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True

app.config['SECRET_KEY'] = 'this is the 1000phone flask secret key'

#文件上传配置
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)),
									"static/img/news/")

#基于app来创建SQLAlchemy 数据库操作实例db
db  = SQLAlchemy(app)

from apps import models

############ SQL Alchemy Settings end############

@app.route('/')
def index():
	return redirect(url_for("home.index"))