
from  urllib.request import urlopen

f = urlopen('https://techcrunch.com')
encoding = f.info().get_content_charset(failobj="utf-8") #content-typeからエンコードを取得

html = f.read().decode(encoding)

print(html)

