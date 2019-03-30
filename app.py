from flask import Flask,render_template,request,flash

app = Flask(__name__)

app.secret_key = 'xs'

'''
目的：实现一个登陆的逻辑处理
（1）路由需要有GET和POST两种方式 ————>需要判断请求方式
（2）获取请求参数
（3）判断参数是否填写 & 密码是否一致
（4）如果判断都没有问题，那么返回success

'''

'''
（1）用flash将错误信息传送到模板中
（2）在模板中也要通过遍历获取flash的消息
（3）对flash消息进行加密，让其他的人无法捕获 通过app.secret_key = ' '  做加密消息混淆






'''
@app.route('/',methods=['GET','POST'])
def hello_world():
    # request:请求对象 -->获取请求方式、数据
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]):
            # print('数据不完整')
            flash('数据不完整')

        elif password != password2:
            # print('密码不一致')
            flash('密码不一致')
        else:
            # print('完成')
            return 'success'
    return render_template('index.html')
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
