from flask import Flask ,request, render_template, make_response

app = Flask(__name__)


@app.route('/login') # 해당 주소를 입력 했을때
def render_login_page() :
    return render_template('login_page.html') # 해당 html 화면을 보여준다.

@app.route('/student_main')
def render_student_main():
    return render_template('stdnt_main.html')

@app.route('/stdnt_learn')
def render_stdnt_learn():
    return render_template('stdnt_learn.html')

@app.route('/teacher_main')
def render_teacher_main():
    return render_template('tcher_main.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3434,debug=True)
    # 현재 이 manage.py 를 Run 시키고,
    # 인터넷 브라우저에 localhost:3434/login 입력하면 첫화면으로 들어가진다. 