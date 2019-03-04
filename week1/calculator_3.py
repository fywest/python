import sys
import csv

class Args(object):
    def __init__(self,args):
        self.configFile,self.userDataFile,self.outputFile=self.get_files(args)

    def get_files(self,args):
        config_list=args
        index_c=config_list.index('-c')
        index_d=config_list.index('-d')
        index_o=config_list.index('-o')
        return config_list[index_c+1],config_list[index_d+1],config_list[index_o+1]

    def __repr__(self):
        return '{}'.format(self.get_files())


class Config(object):
    def __init__(self,configfile):
        self._config=self._read_config(configfile)

    def _read_config(self,configfile):
        config={}
        with open(configfile) as f:
            for line in f.readlines():
                key,value=line.split('=')
                config[key.strip()]=float(value.strip())
        return config

    def get_config(self,key):
        return self._config[key]

    def __repr__(self):
        return '{}'.format(self._config)


class UserData(object):
    def __init__(self,userdatafile):
        self.userdata=self._read_users_data(userdatafile)

    def _read_users_data(self,userdatafile):
        userdata=[]
        with open(userdatafile) as f:
            for line in f.readlines():
                user_id,salary=line.split(',')
                userdata.append((user_id.strip(),int(salary.strip())))
        return userdata

        
    def calculator(self):
        pass

    def dumptofile(self,outputfile):
        pass

    def __repr__(self):
        return '{}'.format(self.userdata)


class IncomeTaxCalculator(object):

    def __init__(self,config,userdata,outputFile):
        self.output_list=[]

    def calc_for_all_userdata(self,config,userdata):
        
        rate=config.get_config('YangLao')+config.get_config('YiLiao')+config.get_config('ShiYe')+config.get_config('GongShang')+config.get_config('ShengYu')+config.get_config('GongJiJin')
        for item in userdata.userdata:
            user_id=item[0]
            line=[]
            base=0
            salary=int(item[1])
            if salary < config.get_config('JiShuL'):
                base = config.get_config('JiShuL')
            elif salary > config.get_config('JiShuH'):
                base = config.get_config('JiShuH')
            else:
                base=salary
           
            insure=self.cal_insure(base,rate)
            amount_tax=salary-insure-3500
            tax=self.cal_tax(amount_tax)
            salary_after_tax=salary-insure-tax
            line.append(user_id)
            line.append(salary)
            line.append(insure)
            line.append(tax)
            line.append(salary_after_tax)
            #print('**********')
            #print(line)
            self.output_list.append(line)
            #print("''''''''''''''''")
            #print(self.output_list)
            #print(self.output_list)
        
        #return self.output_list

    def cal_insure(self,base,rate):
        return base*rate


    def cal_tax(self,amount_tax):
        if amount_tax<=0:
            tax=0
        elif amount_tax>80000:
            tax=amount_tax*0.45-13505
        elif amount_tax>55000:
            tax=amount_tax*0.35-5505
        elif amount_tax>35000:
            tax=amount_tax*0.30-2755
        elif amount_tax>9000:
            tax=amount_tax*0.25-1005
        elif amount_tax>4500:
            tax=amount_tax*0.20-555
        elif amount_tax>1500:
            tax=amount_tax*0.10-105
        else:
            tax=amount_tax*0.03-0

        return tax


    def __repr__(self):
        return '{}'.format(self.output_list)

    def export(self,outputFile):
        #with open("/home/fywest/git/python/week1/gongzi.csv",'w') as f:
        with open(outputFile,'w') as f:
            writer=csv.writer(f)
            #print("export")
            #print(self.output_list)
            writer.writerows(self.output_list)


if __name__=='__main__':
    if len(sys.argv[1:])<6:
        print("Please check -c -d -o parameters")
        exit(-1)

    args=Args(sys.argv[1:])
    #configFile,userDataFile,outputFile=config_args.get_files()
    #print('{},{},{}'.format(configFile,userDataFile,outputFile))
    #print(config_args)

    config=Config(args.configFile)
    #print(config)

    userdata=UserData(args.userDataFile)
    # print(userdata)

    calculator=IncomeTaxCalculator(config,userdata,args.outputFile)
    #calculator.calc_for_all_userdata(config,userdata)
    calculator.export(args.outputFile)
    print(calculator)

