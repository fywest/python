from flask import Flask, render_template, abort

app=Flask(__name__)


@app.route('/')
def index():
    return '<h1> please input user/username </h1>'

@app.route('/user/<username>')
def user_index(username):
    if username=='invalid':
        abort(404)
    return render_template('user_index.html',username=username)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
