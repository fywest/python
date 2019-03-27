#!/bin/bash
echo "run flask"
google-chrome http://localhost:3000/ &
google-chrome -new-tab http://localhost:3000/title &
google-chrome -new-tab http://localhost:3000/files/helloworld &
flask run --port 3000
