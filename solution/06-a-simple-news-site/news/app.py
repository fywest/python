import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)

class Files(object):
    directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"files")

    def __init__(self):
        self._files = self._read_all_files()

    def _read_all_files(self):
        result = {}
        for filename in os.listdir(Files.directory):
            file_path=os.path.join(Files.directory,filename)
            with open(file_path) as f:
                result[filename[:-5]] = json.load(f)
        return result

    def get_title_list(self):
        return [item['title'] for item in self._files.values()]

    def get_by_filename(self,filename):
        return self._files.get(filename)

files = Files()

if __name__=='__main__':
    print(files._files)
    print('*'*20)
    print(files.get_title_list())
    print('*'*20)
    print(files.get_by_filename('helloshiyanlou'))
    print(files.get_by_filename('helloworld'))

