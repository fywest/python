#!/bin/bash
echo "run flask"
google-chrome http://localhost:5000/ &
google-chrome -new-tab http://localhost:5000/title &
google-chrome -new-tab http://localhost:5000/files/helloworld &
flask run
