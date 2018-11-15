# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/29 上午9:30' 

from flask  import Flask


application = Flask(__name__)   #一定要创建Flask实例 application


@application.route('/index')
def IndexHandler():
	return 'hello.'




application.run(port=8889, debug=True)   #启动application