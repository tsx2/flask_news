# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/5/18 下午3:39' 


from apps.models import News
from apps import db

class FlaskDbHelper(object):
	def create_db_table(self):
		db.create_all()
		print("create db ok")


	def query_dataset(self, Cls):
		return Cls.query.all()


	def add_record(self, inst):
		try:
			db.session.add(inst)
			db.session.commit()
			return True
		except Exception as e:
			return False


if __name__ == "__main__":
	fh = FlaskDbHelper()
	fh.create_db_table()

	# ns = News(id=1, title='刘德华结婚了', content='全民偶像刘德华今天结婚了',
	# 		  types='娱乐',image='1.jpg',author='zhougy',view_count=100)
	# fh.add_record(ns)
	# ds = fh.query_dataset(News)
	# for d in ds:
	# 	print(d.to_dict())


