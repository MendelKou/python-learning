'''
用MVC模式实现一个web小应用
安装jinja2模板：pip install jinja2
模板文件放到同级的templates目录下
'''
from flask import Flask,request,render_template

app = Flask(__name__)

#首页
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
#登录
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('signin_form.html')
#登录提交
@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'kmd' and password == 'kmd123':
        model = {
            'username' : username
        }
        return render_template('signin_ok.html',**model)
    else:
        return render_template('signin_form.html',
            username=username,
            message='Incorrect username or password'
        )

if __name__ == '__main__':
    app.run()
