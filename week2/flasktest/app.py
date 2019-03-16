from flask import Flask, render_template
from flask import url_for
from flask import redirect
from flask import request

app=Flask(__name__)

@app.route('/')
def index():
    course= {
        'python':'lou+ python',
        'java':'java base',
        'bigdata':'spark sql',
        'teacher':'shixiaolou',
        'is_unique':False,
        'has_tag':False,
        'tags':['c','c++','docker'],
    }
    return render_template('index.html',course=course)#'hello world'

@app.route('/courses/<course_name>')
def show_course(course_name):
    return 'Course {}'.format(course_name)


@app.route('/test')
def test():
    print(url_for('show_course',course_name='java',_external=True))
    return redirect(url_for('index'))

@app.route('/httptest',methods=['GET','POST'])
def httptest():
    print('method:', request.method)
    if request.method=='POST':
        print('Q: ',request.form.getlist('Q'))
        return 'It is a post request!'
    elif request.method=='GET':
        print('t: ', request.args.get('t'))
        print('q: ',request.args.get('q'))
        return 'It is a get request!'
    else:
        return 'somethong wrong'

if __name__=='__main__':
    app.run()
