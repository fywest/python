import sys

def cal_tax(amount_fortax):

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
        
    return tax

def cal_insure(amount):
    pension=0.08
    medical=0.02
    unemployment=0.005
    injury=0
    maternity=0
    house=0.06
    insure_rate=pension+medical+unemployment+injury+maternity+house
    amount_insure=amount*insure_rate
    return amount_insure

if __name__=='__main__':
    if len(sys.argv)<2:
        print("please input salary amount")
        exit(1)
    #print(sys.argv)
    dict_tax={}
    tax=0.0

    try:
        for arg in sys.argv[1:]:
            key,value=arg.split(':')
            dict_tax[key]=int(value)

      
        for key,value in dict_tax.items():
            insure=cal_insure(value)
            #print(insure)
            amount_tax=value-insure-3500
            if value<3500:
                tax=0
            else:
                tax=cal_tax(amount_tax)
            #print(tax)
            #print(value-insure-tax)

            print("{0}:{1:.2f}".format(key,value-insure-tax))
        exit(0)
    except ValueError:
        print("Parameter Error")
        exit(1)
