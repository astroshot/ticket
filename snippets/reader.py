# coding=utf-8
"""
"""

import lxml.etree as etree
import requests

__save_file_name = '丧病大学.txt'
out_file = open('./' + __save_file_name, 'a+')


def is_blank(s):
    if not s:
        return True
    if not isinstance(s, str):
        raise TypeError('s: {} should be str'.format(s))

    if len(s) < 1:
        return True
    for ch in s:
        if ch != ' ' or ch != '\n' or ch != '\r':
            return False
    return True


def get_page(i):
    base = 7152189
    url = 'http://bequgew.com/20127/{}.html'.format(base + i)
    headers = {
        'Host': 'www.bequgew.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        # 'If-Modified-Since': 'Thu, 19 Dec 2019 06:04:58 GMT',
        # 'If-None-Match': 'W/\"5dfb130a-4cb8\"',
        'Cache-Control': 'max-age=0',
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    if res.status_code != 200:
        print('response status is not 200, url: {}'.format(url))
        return

    body = res.text
    selector = etree.HTML(body)
    title = selector.xpath('/html/body/div[6]/div[1]/h1/text()')
    print(title)
    content = selector.xpath('//*[@id="book_text"]/text()')
    if not content:
        print('no content')
        return

    out_file.write('Chapter {}\n'.format(i))
    for item in content:
        item = item.replace('\r\n', '')
        item = item.replace('\n', '')
        if is_blank(item):
            continue
        # print(item)
        out_file.write(item)
        out_file.write('\n')

    out_file.write('\n\n')


def get_all_novels():
    chapter_count = 113
    for i in range(chapter_count):
        get_page(i + 1)
    out_file.close()


if __name__ == '__main__':
    # get_page(1)
    get_all_novels()
