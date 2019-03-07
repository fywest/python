import sys
import csv
import os

import json

import getopt
from configparser import ConfigParser
from datetime import datetime

class Args(object):
    def __init__(self,args):
        self._params=self.get_files(args)

    def get_files(self,args):
        params={}# cityname config userdata output
        try:
            opts,args=getopt.getopt(args,'C:c:d:o:h',['City=','config=','data=','output=','help'])
        except getopt.GetoptError:
                print('except here')
                sys.exit(2)
        for opt,arg in opts:
            if opt in ('-h','--help'):
                print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
            elif opt in ('-C','--city'):
                params['cityname']=arg
            elif opt in ('-c','--config'):
                params['config']=arg
            elif opt in ('-d','--data'):
                params['userdata']=arg
            elif opt in ('-o','--output'):
                params['output']=arg
            else:
                print('please parameter')
                exit(2)
        return params

    def get_name(self,key):
        return self._params[key]

    def __repr__(self):
        return json.dumps(self._params)

class Config(object):
    def __init__(self,configfile,cityname):
        self._config=self._read_config(configfile,cityname)

    def _read_config(self,configfile,cityname):
        config_dict={}
        config = ConfigParser()
        config.read(configfile,encoding='UTF-8')
        cityname=cityname.upper()
        city_origin_name=cityname
        if cityname not in config.sections():
            cityname='DEFAULT'
            print("{} is not exist in config file and use default value".format(city_origin_name))
        
        print("cityname is : {}".format(cityname))
        list_config=config.items(cityname)
        for item in list_config:
            config_dict[item[0].strip()]=float(item[1].strip())
        return config_dict

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

    def __repr__(self):
        return '{}'.format(self.userdata)


class IncomeTaxCalculator(object):

    def __init__(self,config,userdata,outputfile):
        self.output_list=self.calc_for_all_userdata(config,userdata)
        self.export(outputfile)

    def calc_for_all_userdata(self,config,userdata):
        output_list=[]
        rate=config.get_config('YangLao'.lower())+config.get_config('YiLiao'.lower())+config.get_config('ShiYe'.lower())+config.get_config('GongShang'.lower())+config.get_config('ShengYu'.lower())+config.get_config('GongJiJin'.lower())
        for item in userdata.userdata:
            user_id=item[0]
            line=[]
            base=0
            salary=int(item[1])
            if salary < config.get_config('JiShuL'.lower()):
                base = config.get_config('JiShuL'.lower())
            elif salary > config.get_config('JiShuH'.lower()):
                base = config.get_config('JiShuH'.lower())
            else:
                base=salary
            insure=self.cal_insure(base,rate)
            amount_tax=salary-insure-3500
            tax=self.cal_tax(amount_tax)
            salary_after_tax=salary-insure-tax
            line.append(user_id)
            line.append(salary)
            line.append("%.2f"%insure)
            line.append("%.2f"%tax)
            line.append("%.2f"%salary_after_tax)

            dt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            line.append(dt)

            output_list.append(line)
        return output_list

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

    def export(self,outputfile):
        with open(outputfile,'w') as f:
            writer=csv.writer(f)
            writer.writerows(self.output_list)
        print('gongzi.csv is created...')


if __name__=='__main__':

    args=Args(sys.argv[1:])
    print(args)
    
#print(args.get_name('cityname'))#'config' 'userdata' 'output'

    config=Config(args.get_name('config'),args.get_name('cityname'))
    print(config)

    userdata=UserData(args.get_name('userdata'))
    print(userdata)

    calculator=IncomeTaxCalculator(config,userdata,args.get_name('output'))
    print(calculator)
