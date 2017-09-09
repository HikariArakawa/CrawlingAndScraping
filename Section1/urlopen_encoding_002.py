import sys
from  urllib.request import urlopen

f = urlopen('https://techcrunch.com')
encoding = f.info().get_content_charset(failobj="utf-8") #content-typeからエンコードを取得
#text/htmlのみの定義になっていて、指定されてない可能性もあるので、デフォルトを指定する

print('encoding:', encoding , file=sys.stderr)

#デコードすると文字化けが綺麗になくなるよ
text = f.read().decode(encoding)

print(text)

#日本語のエンコーディングは必ずutf-8とは限らない
#