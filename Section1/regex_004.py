import re

match = re.search(r'a.*c','hogehogeabcd')
print(match)

match = re.search(r'a.*c','hogehogeabCd')
print(match)

match = re.search(r'a(.*)c','hogalianceehogeabcd',re.IGNORECASE)
print(match)
print(match.group(0))
print(match.group(1))


result = re.findall(r'\w{2,}','Lay It All On Me')
print(result)

result = re.sub(r'\w{3,}','Once','Lay It All On Me')
print(result)
