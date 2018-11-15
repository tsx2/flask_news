# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/8/1 下午2:49' 

from flask import Response, render_template, redirect, url_for, flash, session, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
from . import backend


#修改文件名称
def change_filename(filename):
    import os, uuid
    fileinfo = os.path.splitext(filename)
    #filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    #return filename
    filename = datetime.now().strftime("%Y%m%d%H%M%S") +  fileinfo[-1]
    return filename


@backend.route("/hello/", methods = ("GET", ))
def hello():
    return 'hello, world, ok.'

#
@backend.route('/', methods = ("GET", ))  #  /admin  ---> /admin/index/
def index():
    print('this is index enter.')
    return redirect('/admin/index/')


@backend.route('/index/', methods=('GET',))  # /admin/index
@backend.route('/index/<int:page>/', methods=('GET',))  #/admin/index/2/
def admin(page=None):
    if page is None:
        page = 1
    from apps.models import News
    page_data = News.query.filter().order_by(News.created_at.desc()).paginate(page=page, per_page=4)
    return render_template('admin/index.html', page_data = page_data)


@backend.route('/add/', methods=('GET', 'POST'))
def add():
    from apps.admin.forms import NewsForm
    from apps.models import News
    from apps import db, app
    form = NewsForm()
    if form.validate_on_submit():  #表单校验
        #image_url = form.img_url.data.filename
        image_url_file = secure_filename(form.img_url.data.filename)
        ch_image_url = change_filename(image_url_file)
        image_url = app.config["UP_DIR"] + ch_image_url
        form.img_url.data.save(image_url)

        new_obj = News(
            title = form.title.data,
            content = form.content.data,
            types = form.types.data,
            img_url = '/static/img/news/' + ch_image_url,
            created_at = datetime.now(),
        )
        db.session.add(new_obj)
        db.session.commit()
        print("新增新闻成功！")
        #flash('新增新闻成功！')
        return redirect(url_for('admin.index'))
    return render_template('admin/add.html', form=form)


@backend.route('/update/<int:pk>/', methods=('GET', 'POST'))
def update(pk):
    from apps.admin.forms import NewsForm
    from apps.models import News
    from apps import db
    new_obj = News.query.get(pk)
    if not new_obj:
        return redirect(url_for('admin'))
    form = NewsForm(obj = new_obj)

    if form.validate_on_submit():  # 表单校验, 数据更新操作
        new_obj.title = form.title.data
        new_obj.content = form.content.data
        new_obj.types = form.types.data

        db.session.query(News).filter_by(id=pk).update({'title':new_obj.title,
                                                               'content':new_obj.content,
                                                               'types':new_obj.types})
        db.session.commit()
        return redirect(url_for('admin.index'))
    return render_template('admin/update.html', form = form)


@backend.route('/delete/<int:pk>/', methods=('GET', 'POST'))
def delete(pk):
    from apps.models import News
    from apps import db
    new_obj = News.query.get(pk)
    if not new_obj:
        return 'error'
    db.session.query(News).filter_by(id=pk).delete()
    db.session.commit()
    return 'ok'
