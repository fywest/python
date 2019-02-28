import sys

def copyfile(src,des):
    with open(src,'r') as src_file:
        with open(des,'w') as des_file:
            for index,line in enumerate(src_file):
                des_file.write('{0} {1}'.format(index,line))

if __name__ == '__main__':
    if (len(sys.argv)<3):
        print("please input name for source file and destination file")
        sys.exit(-1)

    copyfile(sys.argv[1],sys.argv[2])
    print('copy is done')
    sys.exit(0)
