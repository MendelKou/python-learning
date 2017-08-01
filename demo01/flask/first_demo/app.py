'''
flask是一个python的web框架
安装flask：pip install flask
'''
from flask import Flask,request

app = Flask(__name__)

#首页
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'
#登录
@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="signin" method="post">
                <p>username:<input type="text" name="username"/></p>
                <p>password:<input type="password" name="password"/></p>
                <p><input type="submit" value="signin"/></p>
            </form>'''
#登录提交
@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'kmd' and password == 'kmd123':
        return 'Welcome'
    else:
        return 'Incorrect username or password'
if __name__ == '__main__':
    app.run()
