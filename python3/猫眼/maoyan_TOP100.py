import requests
from requests.exceptions import RequestException
import re  #re正则模块
import json
#from multiprocessing import Pool  #进程池

# 可选是否使用代理
'''
proxies = {
    'https':'119.7.75.172:808'
}
'''

def get_one_page(url):
    try:
        response = requests.get(url, proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
    
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<img data'
                         + '.*?src="(.*?)".*?</a>.*?name"><a.*?>(.*?)</a>.*?class="star">(.*?)</p>'
                         + '.*?releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>.*?</dd>', re.S)
    
    items = re.findall(pattern, html)
    #print(items)
    for item in items:
        yield{
            'paiming': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'pingfen': item[5] + item[6]
        }

def write_to_file(content):
    with open('猫眼.txt', 'a', encoding = 'utf8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    #print(html)  #打印html页面
    for item in parse_one_page(html):
        #print(item)
        write_to_file(item)

if __name__ =='__main__':
    for i in range(10):
        main(i*10)
