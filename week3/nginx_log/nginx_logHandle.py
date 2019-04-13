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
        dict_item['time']=item[1]
        dict_item['url']=item[2]
        dict_item['code']=int(item[3])
        list_log.append(dict_item)

    ip_dict={}
    ip_dict_max={}
    ip_set=set()

    url_dict={}
    url_dict_max={}
    url_set=set()

    max_value=0
    
    for item in list_log:
        date_str=re.findall(r'(.+)\s',item['time'])
        date=datetime.strptime(date_str[0],'%d/%b/%Y:%H:%M:%S')
        if date.date() == datetime(2017,1,11,1,1).date():
            if item['ip'] not in ip_set:
                ip_dict[item['ip']]=1
                ip_set.add(item['ip'])
            else:
                ip_dict[item['ip']]+=1
        
        if item['code']==404:
            if item['url'] not in url_set:
                url_dict[item['url']]=1
                url_set.add(item['url'])
            else:
                url_dict[item['url']]+=1

    for key,value in ip_dict.items():
#print (key,value)
        if value>max_value:
            max_value=value
            ip_dict_max[key]=value
#print(ip_dict_max)        
    
    max_value=0
    for key,value in url_dict.items():
#print (key,value)
        if value>max_value:
            max_value=value
            url_dict_max[key]=value
#print(url_dict_max)        

    return ip_dict_max,url_dict_max

if __name__=='__main__':
    ip_dict,url_dict = main()
    print(ip_dict, url_dict)
