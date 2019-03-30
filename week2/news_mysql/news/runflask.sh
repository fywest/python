#!/bin/bash
echo "run flask"
google-chrome http://localhost:5000/ &
google-chrome -new-tab http://localhost:5000/files/1&
google-chrome -new-tab http://localhost:5000/files/2 &
flask run
