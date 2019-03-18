from flask import Flask, render_template
import json
import os

app=Flask(__name__)

#declare dict object
helloshiyanlou_dict={}
helloworld_dict={}

#get a list of files under folder
files_list=[]
files_list=os.listdir('../files')
print(files_list)

#open json file
with open('../files/helloshiyanlou.json','r') as file:
    helloshiyanlou_dict = json.loads(file.read())
print (helloshiyanlou_dict)

with open('../files/helloworld.json','r') as file:
    helloworld_dict = json.loads(file.read())
print (helloworld_dict)

@app.route('/')
def index():
    pass

@app.route('/files/<filename>')
def file(filename):
    pass
