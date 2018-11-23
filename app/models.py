from app.ext import db



# 用户模型类
class User(db.Model):
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 用户名
    name = db.Column(db.String(40))
    # 密码
    password = db.Column(db.String(256))
    # 邮箱
    email = db.Column(db.String(40), unique=True)
    # 令牌
    token = db.Column(db.String(256))
    # 是否删除
    isdelete = db.Column(db.Boolean, default=False)
    # 是否激活
    isactive = db.Column(db.Boolean, default=False)
    # 头像
    icon = db.Column(db.String(40), default='head.png')
    # 等级
    permissions = db.Column(db.Integer, default=1)


class Wheel(db.Model):
    bannerid = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256))


class Movies(db.Model):
    postid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    like_num = db.Column(db.Integer, default=0)
    share_num = db.Column(db.Integer, default=0)
    image = db.Column(db.String(256))
    publish_time = db.Column(db.String(256))
    rating = db.Column(db.Float)
    duration = db.Column(db.String(40))
    app_fu_title = db.Column(db.String(40))
    request_url = db.Column(db.String(256),default='')


class Like(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    u_id = db.Column(db.Integer,db.ForeignKey(User.id))
    m_id = db.Column(db.Integer,db.ForeignKey(Movies.postid))
