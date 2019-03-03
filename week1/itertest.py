testlist=['Linux','Java','Python','DevOps','Go']
it=iter(testlist)

print("Loop start")

while True:
    try:
        course=next(it)
        print(course)
    except StopIteration:
        print("Loop End")
        break


