from flask import Flask
from app.ext import init_ext
from app.settings import init_app
from app.views import init_blue


def create_app(env_name='default'):
    app = Flask(__name__)

    # 配置
    init_app(app, env_name)

    # 扩展
    init_ext(app)

    # 蓝图
    init_blue(app)

    return app
