#!/bin/bash
#let us call this script py3.sh
rm /home/fywest/git/python/week1/gongzi_new.csv
sleep 1
python3 calculator_6.py -C chengdu -c test_new.cfg -d user_new.csv -o gongzi_new.csv
