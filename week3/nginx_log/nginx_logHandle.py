import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                r'\[(.+)\]\s'
                r'"GET\s(.+)\s\w+/.+"\s'
                r'(\d+)\s'
                r'(\d+)\s'
                r'"(.+)"\s'
                r'"(.+)"'
                )
        parsers = re.findall(pattern,logfile.read())

    return parsers

def main():
    logs = open_parser('/home/fywest/git/python/week3/nginx_log/nginx.log')
    list_log=[]
    for item in logs:
        dict_item={}
        dict_item['ip']=item[0]
#time_str=re.findall(r'(.+)\s',item[1])
#time=datetime.strptime(time_str[0],'%d/%b/%Y:%H:%M:%S')
        dict_item['time']=item[1]
        dict_item['url']=item[2]
        dict_item['code']=int(item[3])
        list_log.append(dict_item)

#print(list_log)
        
    ip_dict={}
    ip_dict_max={}
    max_value=0

    url_dict={}

    ip_set=set()
    for item in list_log:
#print(item['time'])
        date_str=re.findall(r'(.+)\s',item['time'])
        date=datetime.strptime(date_str[0],'%d/%b/%Y:%H:%M:%S')
#print(date)
#print(date.date())
#print(datetime(2017,1,11,1,1).date())
#print(ip_set)
        if date.date() == datetime(2017,1,11,1,1).date():
#print(item)
            if item['ip'] not in ip_set:
                ip_dict[item['ip']]=0
                ip_set.add(item['ip'])
            ip_dict[item['ip']]+=1



    for key,value in ip_dict.items():
        print (key,value)
        if value>max_value:
            max_value=value
            ip_dict_max[key]=value

    print(ip_dict_max)        


    return ip_dict,url_dict

if __name__=='__main__':
    ip_dict,url_dict = main()
#print(ip_dict, url_dict)
