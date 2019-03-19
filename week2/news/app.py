from flask import Flask, render_template
import json
import os

app=Flask(__name__)


books={}
def get_books():
    global books
    #get a list of files under folder
    files_list=[]
    files_list=os.listdir('../files')
    #print(files_list)
    for file_item in files_list:
        #open json file
        with open('../files/'+file_item,'r') as file:
            book_dict = json.loads(file.read())
            books[file_item]=book_dict
   
titles=[]
def get_titles():
    for filename,book in books.items():
        titles.append(book['title'])

book=''
def get_content(filename):
    get_books()
    for name,book in books.items():
        print(name,filename)
        if filename==name:
            return book['content']

@app.route('/')
def index():
    get_books()
    return render_template('index.html',books=books)

@app.route('/title')
def index_title():
    get_books()
    get_titles()
    return render_template('index.html',titles=titles)
    
@app.route('/files/<filename>')
def file(filename):
    get_books()
    book=get_content(filename)
    print(book)
    return render_template('index.html',book=book)

if __name__=='__main__':
    get_books()
    print('books below')
    print(books)
    print('*'*20)
    get_titles()
    print(titles)
    book=get_content('helloworld.json')
    print(book)
    app.run()
