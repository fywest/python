#!/bin/bash
rm /home/fywest/git/python/week1/gongzi.csv
sleep 1
python3 challenge3.py -c test.cfg -d user.csv -o gongzi.csv
