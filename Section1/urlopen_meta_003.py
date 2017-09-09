import re
import sys
from urllib.request import urlopen
#ヘッダからContents-typeが取れなかったときどうする？
f = urlopen('https://techcrunch.com/popular/')
bytes_content = f.read()
#<meta charset="UTF-8"> がここらへんにあると予測してやる
scanned_text = bytes_content[:4096].decode('ascii', errors='replace')

#「charset="(or ')」 以降の非文字(空白/改行)以外へのマッチ
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

if match:
    # マッチする場合は指定エンコーディングを使用
    encoding = match.group(1)
else:
    # 見つからない場合はデフォルトで utf-8 に決め打ち
    encoding = 'utf-8'

print('encoding:',encoding, file=sys.stderr)

text = bytes_content.decode(encoding)

print(text)
#エンコーディングされているものはデコードする
#エンコードはmetaタグに書いているか、ヘッダーに書いてあるか、どちらかを確認する