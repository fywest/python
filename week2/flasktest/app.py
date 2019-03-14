from flask import Flask
from flask import url_for
from flask import redirect

app=Flask(__name__)
@app.route('/')
def index():
    return 'hello world'

@app.route('/courses/<course_name>')
def show_course(course_name):
    return 'Course {}'.format(course_name)


@app.route('/test')
def test():
    print(url_for('show_course',course_name='java',_external=True))
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run()
