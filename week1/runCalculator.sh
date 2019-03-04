#!/bin/bash
#let us call this script py3.sh
rm /home/fywest/git/python/week1/gongzi.csv
sleep 1
python3 ./calculator_5.py -c /home/fywest/git/python/week1/test.cfg -d /home/fywest/git/python/week1/user.cfg -o /home/fywest/git/python/week1/gongzi.csv
