import os


if __name__=='__main__':
    dirname='/home/fywest/tmp/syl'
    os.mkdir(dirname)
    filename='__init__.py'
    filepath=os.path.join(dirname,filename)
    with open(filepath,'w') as f:
        pass
    for folder in ['A','B','C']:
        dirname_temp=dirname+'/'+folder
        os.mkdir(dirname_temp)
        filepath_temp=os.path.join(dirname_temp,'__init__.py')
        with open(filepath_temp,'w') as f:
            pass



