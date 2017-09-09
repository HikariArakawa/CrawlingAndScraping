from urllib.request import urlopen

#f = urlopen('https://gihyo.jp/dp')
f = urlopen('https://docs.docker.com/reference/')
print('DataType:' + str(type(f)))
print('Body:')
print(f.read())
print('HTTP Status' + str(f.status))
print(f.getheader('Content-Type'))
