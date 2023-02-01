import data as d
from random import randint
from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps


def main(data):
    rnd = randint(0, len(data)-1)
    str_txt = data[rnd][:-1].replace(r"\n", "\n")
    return str_txt


def weather(txt):
    text = ''
    owm = OWM('05a8c98f2471198e605522333cbc6e13')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(txt)
    w = observation.weather
    tempetature = w.temperature('celsius')['temp']
    return ('В городе ' + txt + ' температура: ' + str(tempetature) + " °С")
