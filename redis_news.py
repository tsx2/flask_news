# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/9/29 上午10:56'

'''
使用redis缓存新闻数据
'''
import redis
from datetime import datetime

# 新闻数据字段配置信息
NEWS_FIELDS = (
	'title', 'img_url', 'content', 'is_valid', 'types', 'created_at', 'updated_at'
)


def datetime_format(datatime_now):
	return datatime_now.strftime("%Y-%m-%d %H:%M:%S")


class Paginate(object):
	'''
	分页功能
	'''
	def __init__(self, data_list, cur_page=1, per_page=1):
		self.__data_list = data_list
		self.__cur_page = cur_page
		self.__per_page = per_page

	@property
	def page(self):
		return self.__cur_page

	@property
	def items(self):
		'''
		获取当前页的数据
		:return:
		'''
		return self.__data_list

	@property
	def has_prev(self):
		'''
		判断是否有上一页
		:return:
		'''
		return self.__cur_page > 1

	@property
	def has_next(self):
		'''
		判断是否有下一页
		:return:
		'''
		return self.__cur_page < len(self.__data_list)

	@property
	def prev_num(self):
		'''
		上一页页码
		:return:
		'''
		return self.__cur_page - 1

	@property
	def next_num(self):
		return self.__cur_page + 1

	def iter_pages(self):
		'''
		返回迭代器的页面
		:return:
		'''
		return range(1, self.__cur_page)


class RedisNews(object):
	def __init__(self):
		'''
		连接redis数据库
		'''
		self.rds = redis.Redis(host="127.0.0.1", port=6379, db=3, decode_responses=True)

	def add_news(self, news_obj):
		'''
		新增新闻数据
		:param news_obj:
		:return:
		'''
		# 通过redis的incr函数产生自增id
		news_tmp_id = self.rds.incr("news_id")
		# 拼接新闻数据key --> hash存储
		news_id = "news:%d" % news_tmp_id
		# 存储新闻id（list）
		self.rds.lpush('news', news_tmp_id)  # 把新闻自增id放入到列表
		# 存储新闻数据 (hash) key---> news_id, value: news_obj (json串)
		result = self.rds.hmset(news_id, news_obj)
		# 存储新闻类别  --- 新闻ID （set）
		news_types = "news_type:%s" % news_obj['types']
		self.rds.sadd(news_types, news_tmp_id)
		return result

	def init_news(self, data_list):
		'''
		批量添加新闻
		:param data_list:  [{}, {}]
		:return:
		'''
		for news in data_list:
			res = self.add_news(news)
			print(res)


list_news = [
	{
		"title": "朝鲜特种部队视频公布 展示士兵身体素质与意志",
		"img_url": "/static/img/news/01.png",
		"content": "新闻内容",
		"is_valid": 1,
		"types":  "推荐",
        "created_at": datetime_format(datetime.now()),
		"updated_at": datetime_format(datetime.now()),
	 },
     {
		"title": "导弹来袭怎么办？日本政府呼吁国民躲入地下通道",
		"img_url": "/static/img/news/03.png",
		"content": "新闻内容",
		"is_valid": 1,
		"types":  "本地",
        "created_at": datetime_format(datetime.now()),
		"updated_at": datetime_format(datetime.now()),
	 },
]

def main():
	redis_news = RedisNews()
	redis_news.init_news(list_news)


main()

