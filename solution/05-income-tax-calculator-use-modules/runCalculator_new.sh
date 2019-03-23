#!/bin/bash
rm /home/fywest/git/python/week1/gongzi.csv
sleep 1
python3 calculator.py -c test.cfg -d user.csv -o gongzi.csv
