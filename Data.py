import requests
import json
import pandas as pd
from pandas.io.json import json_normalize


r = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1581300800&end=1589581187&period=300")
#  Récupération des données de BTC en USD 
# (start et end représente la plage horaire désirée en secondes, period l'unité de temps d'une bougie, ici 300 sec)

parsed = json.loads(r.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r._content)

res = json_normalize(a)
##print(res)

df = pd.DataFrame(res) #Création d'un dataframe récupérant les données
print(df)

##df = pd.read_json(a)
##print(df)'''


r1 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1574300800&end=1581300799&period=300")
parsed = json.loads(r1.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r1._content)

res = json_normalize(a)
##print(res)

df1 = pd.DataFrame(res)
print(df1)

##df = pd.read_json(a)
##print(df)'''


r2 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1567300800&end=1574300799&period=300")
parsed = json.loads(r2.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r2._content)

res = json_normalize(a)
##print(res)

df2 = pd.DataFrame(res)
print(df2)

##df = pd.read_json(a)
##print(df)'''


r3 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1560300800&end=1567300799&period=300")
parsed = json.loads(r3.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r3._content)

res = json_normalize(a)
##print(res)

df3 = pd.DataFrame(res)
print(df3)

##df = pd.read_json(a)
##print(df)'''

r4 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1553300800&end=1560300799&period=300")
parsed = json.loads(r4.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r4._content)

res = json_normalize(a)
##print(res)

df4 = pd.DataFrame(res)
print(df4)

##df = pd.read_json(a)
##print(df)'''


r5 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1546300800&end=1553300799&period=300")
parsed = json.loads(r5.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r5._content)

res = json_normalize(a)
##print(res)

df5 = pd.DataFrame(res)
print(df5)

##df = pd.read_json(a)
##print(df)'''


r6 = requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_BTC&start=1539300800&end=1546300799&period=300")
parsed = json.loads(r6.text)

print (json.dumps(parsed, indent=2, sort_keys=True))


a = json.loads(r6._content)

res = json_normalize(a)
##print(res)

df6 = pd.DataFrame(res)
print(df6)

##df = pd.read_json(a)
##print(df)'''

dff = pd.concat([df1,df2,df3,df4,df5,df6], ignore_index=True) #Récupère les données des différents DataFrame pour les mettres dans 1 seul

