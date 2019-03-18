from flask import Flask, render_template
import json

app=Flask(__name__)

#declare dict object
helloshiyanlou_dict={}
helloworld_dict={}

#open json file
with open('./files/helloshiyanlou.json','r') as file:
    helloshiyanlou_dict = json.loads(file.read())
print (helloshiyanlou_dict)

with open('./files/helloworld.json','r') as file:
    helloworld_dict = json.loads(file.read())
print (helloworld_dict)

@app.route('/')
def index():
    pass

@app.route('/files/<filename>')
def file(filename):
    pass
