# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:50' 

from flask_sqlalchemy import SQLAlchemy
from apps import db
from datetime import datetime

class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    types = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(300))
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    is_valid = db.Column(db.Boolean,default=0)

    def __str__(self):
        return self.title


    def to_dict(self):
        return dict(title=self.title, content=self.content,
                    news_type=self.types, img_url=self.image, author=self.author,
                    view_count=self.view_count, created_at=self.created_at)
