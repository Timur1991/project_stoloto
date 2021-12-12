import requests
import pandas as pd
import time
from pandas import ExcelWriter

url = "https://www.stoloto.ru/p/api/mobile/api/v34/service/draws/archive"

# дата в формате месяц/день/год
date_range = pd.period_range(start="9/29/2021", end="12/6/2021", freq="D")
# date_range = pd.period_range("10/15/2021", "11/11/2021", freq="D")
date_range = pd.period_range(start="9/13/2021", end="10/26/2021", freq="D")
data = []
for date in date_range:
    print(f'Сбор данных на {date}...')
    querystring = {"count": "50", "game": "keno2", "date_from": f"{date}", "date_to": f"{date}",
                   "superprize": "false", "second_prize": "false"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
        "Device-Type": "MOBILE",
        "Gosloto-Partner": "bXMjXFRXZ3coWXh6R3s1NTdUX3dnWlBMLUxmdg",
        "Connection": "keep-alive",
        "Referer": "https://www.stoloto.ru/keno2/archive/",
        "Cookie": "isgua=false; _SI_VID_1.6befd9a02400013179aba889=e234e776b030db4e9b7a9743; K=1638458176471; welcome=true; _SI_DID_1.6befd9a02400013179aba889=213bdbd1-b80e-330e-be96-b34d1a1f1add; _SI_SID_1.6befd9a02400013179aba889=f6d2882974dd4821c3fb3b24.1638601170123.1256067; gjac=true",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    datas_json = response.json()
    for json_data in datas_json["draws"]:
        data.append({
            'Тираж': json_data["number"],
            'Дата': json_data["date"].split('T')[0],
            'Время': json_data["date"].split('T')[-1].split('+')[0],
            'Выплата': json_data["summPayed"],
            '1': json_data["winningCombination"][9],
            '2': json_data["winningCombination"][10],
            '3': json_data["winningCombination"][11],
            '4': json_data["winningCombination"][12],
            '5': json_data["winningCombination"][13],
            '6': json_data["winningCombination"][14],
            '7': json_data["winningCombination"][15],
            '8': json_data["winningCombination"][16],
            '9': json_data["winningCombination"][17],
            '10': json_data["winningCombination"][18],
            '11': json_data["winningCombination"][19],
            '12': json_data["winningCombination"][20],
            '13': json_data["winningCombination"][21],
            '14': json_data["winningCombination"][22],
            '15': json_data["winningCombination"][23],
            '16': json_data["winningCombination"][24],
            '17': json_data["winningCombination"][25],
            '18': json_data["winningCombination"][26],
            '19': json_data["winningCombination"][27],
            '20': json_data["winningCombination"][28],
        })
    # time.sleep(1)
print(f'Данные с {date_range[0]} по {date_range[-1]} собраны')
# запись в эксель
dataframe = pd.DataFrame(data)
writer = ExcelWriter(f"Результат игр с {date_range[0]} по {date_range[-1]}.xlsx")
dataframe.to_excel(writer, 'data', index=False)
writer.save()
print(f'Итоговый файл: "Результат игр с {date_range[0]} по {date_range[-1]}.xlsx"')
print(f'Собранно тиражей: {len(data)}')
