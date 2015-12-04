from urllib import request, parse

def fetch_xml(url):
    with request.urlopen(url) as f:
        data = f.read()
    return data.decode('utf-8')


# 测试
print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))