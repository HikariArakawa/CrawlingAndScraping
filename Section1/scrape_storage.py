import re
from urllib.request import urlopen
from html import unescape
import json

URL = 'https://techcrunch.com/popular/'
CSV_PATH = 'csv_storage.csv'


def fetch(url):
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)

    return html


def scrape(html):
    data = []
    """正規表現を用いたスクレイピング"""
    for topic in re.findall(r'<a href=.* class="trending-post">[\s\S]*?</a>', html):
        url_tmp = re.search(r'<a href=(.*) class="trending-post">', topic)
        title_tmp = re.search(r'<div class="trending-title">([\s\S]*?)</div>', topic)
        title = title_tmp.group(1).strip()
        title = unescape(title)     #文字参照を記号に戻す
        url = url_tmp.group(1).strip()

        print(','.join([title, url])) #ログがわり

        data.append({
            'title': title,
            'url': url
        })

    return data

def output_json(source_dic):
    data_json = json.dumps(source_dic, ensure_ascii=False, indent=2)
    print(data_json)

def output_csv(source_dic):
    with open(CSV_PATH, "w", encoding='utf-8') as o:
        for data in source_dic:
            o.write(','.join(['"{}"'.format(data['title']), data['url']]))
            o.write('\n')




def main():
    html = fetch(URL)
    topics = scrape(html)

    output_json(topics)
    output_csv(topics)



if __name__ == '__main__':
    main()
