from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    pass


@app.route('/files/<filename>')
def file(filename):
    pass
