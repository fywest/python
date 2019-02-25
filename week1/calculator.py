import sys

if __name__=='__main__':
    if len(sys.argv)<2:
        print("please input salary amount")
        exit(1)
    print(sys.argv[1])
    try:
        amount=int(sys.argv[1])
        tax=0.0
        amount_fortax=0.0
        amount_fortax=amount-0-3500
        if amount_fortax<=0:
            tax=0;
        elif amount_fortax>80000:
            tax=amount_fortax*0.45-13505
        elif amount_fortax>55000:
            tax=amount_fortax*0.35-5505
        elif amount_fortax>35000:
            tax=amount_fortax*0.30-2755
        elif amount_fortax>9000:
            tax=amount_fortax*0.25-1005
        elif amount_fortax>4500:
            tax=amount_fortax*0.20-555
        elif amount_fortax>1500:
            tax=amount_fortax*0.1-105
        else:
            tax=amount_fortax*0.03-0

        print("{0:.2f}".format((tax)))
        exit(0)
    except ValueError:
        print("Parameter Error")
        exit(1)
