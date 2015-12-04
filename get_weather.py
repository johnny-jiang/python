#get_weather.py
from urllib import request, parse
from xml.parsers.expat import ParserCreate
from datetime import datetime


def fetch_xml(url):
    with request.urlopen(url) as f:
        data = f.read()
    return data.decode('utf-8')

class WeatherSaxHandler(object):

    def __init__(self):
        self._weather={}
        self._weather['today']={}
        self._weather['tomorrow']={}

    @property
    def weather(self):
        return self._weather

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self._weather.update(attrs)
        elif name == 'yweather:forecast':
            tday=datetime.now()
            date=datetime.strptime(attrs['date'],'%d %b %Y')
            delta=date-tday
            if delta.days==0:
                self._weather['today'].update(attrs)
                self._weather['today']['low']=int(attrs['low'])
                self._weather['today']['high']=int(attrs['high'])
            elif delta.days==1:
                self._weather['tomorrow'].update(attrs)
                self._weather['tomorrow']['low']=int(attrs['low'])
                self._weather['tomorrow']['high']=int(attrs['high'])
            # else :
            # self._weather[attrs['date']]=attrs


    def end_element(self, name):
        pass

    def char_data(self, text):
        pass
woeid_changcchun=2137321
woeid_beijing=2151330
data=fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2137321')
handler = WeatherSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(data)
weather=handler.weather
print(weather['city'],weather['region'],weather['country'])
print(weather['today'])
print(weather['tomorrow'])

