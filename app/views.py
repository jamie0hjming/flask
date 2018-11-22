from flask import Blueprint, render_template, request, redirect, session, url_for, g,jsonify
# from flask.json import jsonify

from app.ext import db
from app.tools import generate_password, genarator_token
from app.models import User

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/index/', methods=['GET'])
def index():

    return render_template('index.html',user =g.user )

@blue.route('/register/', methods=['POST'])
def register():
    account = request.form.get('account')
    password = request.form.get('password')
    nick_name = request.form.get('nick_name')
    check_pwd = request.form.get('check_pwd')
    user = User()
    user.email = account
    user.name = nick_name
    user.password = generate_password(password)
    token = genarator_token()
    user.token = token
    db.session.add(user)
    db.session.commit()
    session['token'] = user.token
    return redirect(url_for('blue.index'))



@blue.route('/check/', methods=['GET'])
def check():
    account = request.args.get('account')
    print(account)
    users = User.query.filter(User.email==account)
    print(users.count())
    data = {}
    if users.count():
        data['status'] = 0
        data['msg'] = '用户名已被注册'
    else:
        data['status'] = 1
        data['msg'] = '用户名可用'
    return jsonify(data)



@blue.route('/login/', methods=['POST','GET'])
def login():

    if request.method == 'POST':
        print(111111)
        account = request.form.get('account_login')
        password = request.form.get('password_login')
        users = User.query.filter(User.email == account).filter(
            User.password == generate_password(password))
        if users:
            user = users.first()
            print(user.email)
            token = genarator_token()
            user.token = token
            db.session.add(user)
            db.session.commit()
            session['token'] = user.token
        else:
            return '登陆失败'
        return redirect(url_for('blue.index'))
    else:
        account = request.args.get('account')
        print(account)
        password = request.args.get('password')
        users = User.query.filter(User.email == account).filter(
            User.password == generate_password(password))
        print(users.count())
        if users.count():
            data = {
                'status':1,
                'msg':'ok',
            }
        else:
            data = {
                'status': 0,
                'msg':'账号或密码错误'
            }
        return jsonify(data)


@blue.before_request
def before():
    token = session.get('token')
    if token:
        user = User.query.filter(User.token == token).first()
    else:
        user = None
    g.user = user


@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect(url_for('blue.index'))