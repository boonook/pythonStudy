import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    try:
        reponse = requests.get(url)
        if reponse.status_code ==200:
            return reponse.text
        return None
    except RequestException:
        return None

def prase_one_page(html):
    # pattern = re.compile('<div>.*?bookname.*?>(.*?)</a>.*?src="(.*?)".*?bookilnk><a'
    #                      +'.*?>(.*?)</a>')
    pattern = re.compile('<div.*?bookbox.*?>.*?bookimg.*?src="(.*?)".*?bookname.*?<a.*?>(.*?)</a>.*?bookintro.*?>(.*?)</div>.*?bookimg.*?>.*?<a.*? href="(.*?)".*?>.*?</a>.*?bookilnk.*?<a.*? href="(.*?)".*?>(.*?)</a>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?</div>',re.S)
    item = re.findall(pattern,html)
    # data = []
    for i in item:
        # print(i[8])
        # print(i[8].strip())
        yield {
            'imgSrc': i[0],
            'bookname': i[1],
            'bookintro': i[2].strip(),
            'bookUrl': i[6],
            'bookZhuozhe': i[5],
            'bookZhuozheUrl': i[4],
            'bookType': i[7],
            'bookStatus': i[8].strip(),
            'bookTime': i[9].strip(),
        }
    # 祛除空格及换行符
    # print(item)

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()


def main(index):
    url = 'http://book.zongheng.com/store/c1/c0/b0/u0/p'+index+'/v9/s1/t0/u0/i1/ALL.html'
    print(url)
    html = get_one_page(url)
    for i in prase_one_page(html):
        write_to_file(i)

if __name__ == '__main__':
    for i in range(1000):
        main('%d' %(i+1))