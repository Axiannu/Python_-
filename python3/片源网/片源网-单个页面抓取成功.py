import re
import requests
import json

proxies = {
        'https': '119.7.75.172:808'
    }

def get_one_page(url):
    response = requests.get(url, proxies)
    return response.text

def parse_one_page(html):
    pattern = re.compile('.*?<tr class="(odd|even)">.*?<img width.*?data-original="(.*?)"'
                         + '.*?<br>(《.*?》)'
                         + '(.*?)</td>'
                         + '.*?nobr center">(.*?)</td>'
                         + '.*?nobr center">(.*?)</td>', re.S)
    items = re.findall(pattern, html)
    #print(items)
    #return items
    for item in items:
        #print(item, sep="\n")
        yield {
            'image': item[1],
            'name': item[2].strip(),
            'actor': item[3].strip(),
            'size': item[4],
            'time': item[5]
        }
def write_data(content):
    with open('片源影单.txt', 'a', encoding='utf8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = "http://pianyuan.la/?p=1"
    html = get_one_page(url)
    #print(html)
    #parse_one_page(html)
    #print(items)
    #for item in items:
    for item in parse_one_page(html):
        write_data(item)

if __name__ == '__main__':
    main()
