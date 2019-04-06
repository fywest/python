# -*- coding: utf-8 -*-
from openpyxl import load_workbook
from openpyxl import Workbook
import datetime

def combine():
    '''
    open workbook xlsx
    select sheet range -student
    active worksheet -student
    loop row and column
    read value from cell
    fill value to student-list for create,course,amount
    
    active worksheet -time
    loop row and column
    read value from cell
    fill value to time-list for create,course,study

    create list combine create,course,amount,study
    fill value based on course name

    create new sheet - combine
    loop row and column
    write list value to cell

    '''

    wb=load_workbook(filename='courses.xlsx')
    ws=wb['students']
    list_student=[]
    for x in range(1,11):
        dict_student={}
        dict_student['create']=(ws.cell(row=x,column=1)).value
        dict_student['course']=(ws.cell(row=x,column=2)).value
        dict_student['study']=(ws.cell(row=x,column=3)).value
        #print(dict_student)   
        list_student.append(dict_student)
    for item in list_student:
        print(item)
 
def split():
    pass

if __name__ == '__main__':
    combine()
    split()
#d.strftime("%Y/%m/%d %H:%M:%S")
