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

