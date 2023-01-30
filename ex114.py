from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('Site não disponível')
else:
    print('Site disponível')
    print(site.read())
