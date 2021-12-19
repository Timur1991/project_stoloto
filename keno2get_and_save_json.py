import json
import requests

url = "https://www.stoloto.ru/p/api/mobile/api/v34/service/draws/archive"

querystring = {"count": "10", "game": "keno2", "date_from": "2021-12-04", "date_to": "2021-12-04"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Type": "application/x-www-form-urlencoded",
    "Device-Type": "MOBILE",
    "Gosloto-Partner": "bXMjXFRXZ3coWXh6R3s1NTdUX3dnWlBMLUxmdg",
    "Connection": "keep-alive",
    "Referer": "https://www.stoloto.ru/keno2/archive",
    "Cookie": "isgua=false; _SI_VID_1.6befd9a02400013179aba889=e234e776b030db4e9b7a9743; K=1638458176471; welcome=true; _SI_DID_1.6befd9a02400013179aba889=213bdbd1-b80e-330e-be96-b34d1a1f1add; _SI_SID_1.6befd9a02400013179aba889=7e012d8bd29ffa2172877bfc.1639933103448.363500; gjac=true",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

response = requests.get(url, headers=headers, params=querystring)

data_json = response.json()

print('Дата проведения тиража: ', data_json["draws"][0]["date"])
print('Номер тиража: ', data_json["draws"][0]["number"])
print('Выпавшие числа тиража: ', data_json["draws"][0]["winningCombination"])
print('Выплата: ', data_json["draws"][0]["summPayed"])

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data_json, file, indent=2, ensure_ascii=False)
    print('Данные сохранены в  json файл')
