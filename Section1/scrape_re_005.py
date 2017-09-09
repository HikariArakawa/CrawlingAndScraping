import re
from html import unescape

with open('/Users/hikariarakawa/WorkSpace/Python/WebScraping/dp.html', encoding='utf-8') as f:
    html = f.read()

    #for url in re.findall(r'<a href=(.*?) class="trending-post">',html):
     #   print(url)


    for topic in re.findall(r'<a href=.* class="trending-post">[\s\S]*?</a>', html):
        url_tmp = re.search(r'<a href=(.*) class="trending-post">', topic)
        title_tmp = re.search(r'<div class="trending-title">([\s\S]*?)</div>', topic)
        title = re.sub(r"&nbsp;|&#8217;"," ", title_tmp.group(1).strip())
        url = url_tmp.group(1).strip()

        print(title)
        print(url)

