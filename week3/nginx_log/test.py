import re
from datetime import datetime


def main():
    str='180.76.15.157 - - [09/Jan/2017:07:44:03 +0800] "GET /s?path=/sbin/lilo&project=linux-3.18.6 HTTP/1.1" 502 181 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'
    print(str)
    pattern = (r''
            r'(\d+.\d+.\d+.\d+)\s-\s-\s'
            r'\[(.+)\]\s'
            r'"GET\s(.+)\s\w+/.+"\s'
            r'(\d+)\s'
            r'(\d+)\s'
            r'"(.+)"\s'
            r'"(.+)"')
    pattern0 = (r'')
    pattern1 = (r'(\d+.\d+.\d+.\d+)\s-\s-\s')
    pattern2 = (r'\[(.+)\]\s')
    pattern3 = (r'"GET\s(.+)\s\w+/.+"\s')
    pattern4 = (r'(\d+)\s')
    pattern5 = (r'(\d+)\s')
    pattern6 = (r'"(.+)"\s')
    pattern7 = (r'"(.+)"')
    parsers = re.findall(pattern,str)
    parsers1 = re.findall(pattern0+pattern1+pattern2+pattern3+pattern4+pattern5+pattern6+pattern7,str)
    print(parsers)
    print(parsers1)

if __name__=='__main__':
    main()
