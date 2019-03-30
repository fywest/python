#!/bin/bash
echo "run flask"
google-chrome http://localhost:3000/ &
google-chrome -new-tab http://localhost:3000/files/1 &
google-chrome -new-tab http://localhost:3000/files/2 &
flask run --port 3000
