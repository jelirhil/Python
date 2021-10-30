
from googletrans.gtoken import TokenAcquirer
import requests 
import json
from googletrans import Translator

translator= Translator()
#acquirer = TokenAcquirer()
cidade = input('Escreva sua cidade:')

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade+ '&appid=cc77e3425c57f3802b4f95c9ee8071b4')

tempo = req.json()
tempo_1 = (tempo['weather'][0]['main'])

tempo_pt = translator.translate(tempo_1,dest='pt')
print (tempo_pt.text)
temp = (tempo['main']['temp']-273.15)
print (f'A temperatura é de {temp:.2f}°')