# app.py

# Flask 클래스 임포트
from flask import Flask

# Flask 클래스 인스턴스화. 애플리케이션의 이름을 매개변수로 전달한다.
# 단일 모듈이라면 __name__ 변수를 사용해야 한다.
app = Flask(__name__)

# 어떤 URL로 함수를 실행할지 지정한다.
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/users')
def get_users():
    return 'users'

# 동적 url 생성
@app.route('/users/<username>')
def get_user_info(username):
    return f"username: {username}"

# 변수의 유형 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# 프로그램 시작점
if __name__ == '__main__':
    # 애플리케이션 실행
    app.run()