from flask import Flask
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/courses/<course_name>')
def show_courses(course_name):
    return 'Courses: {}'.format(course_name)

@app.route('/test')
def test():
    print('in test fun')
    print(url_for('index'))
    print(url_for('user_index',username='shiyanlou'))
    print(url_for('show_post',post_id=1,_external=True))
    print(url_for('show_post',post_id=2, q='python 03'))
    print(url_for('show_post',post_id=3, q='python ok'))
    print(url_for('show_post',post_id=4, _anchor='a'))
    return 'test'

@app.route('/<username>')
def hello(username):
    if username=='shiyanlou':
        return 'hello {}'.format(username)
    else:
        return redirect(url_for('index'))



if __name__=='__main__':
    app.run()
