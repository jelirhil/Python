
from googletrans.gtoken import TokenAcquirer
import requests 
import json
from googletrans import Translator

#ativa tradutor
translator= Translator()
#escolha a cidade
cidade = input('Escreva sua cidade:')
#requer da API
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade+ '&appid=cc77e3425c57f3802b4f95c9ee8071b4')
#altera para json
tempo = req.json()
#recebe a temperatura e transforma em Celsius, era kelvin
temp = (tempo['main']['temp']-273.15)
tempo_1 = (tempo['weather'][0]['main'])
#traduz
tempo_pt = translator.translate(tempo_1,dest='pt')

print (tempo_pt.text)
print (f'A temperatura é de {temp:.2f}°')
