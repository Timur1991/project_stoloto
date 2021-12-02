from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import pandas as pd
from datetime import datetime
from pandas import ExcelWriter
#pip install openpyxl


# сбор архива тиражей игры кено и сохр  в эксель файл


def get_content():
    print('Запуск браузера в фоновом режиме...')
    # browser = webdriver.Chrome('chromedriver/chromedriver')
    options = webdriver.ChromeOptions()
    # добавим свой user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")
    # можно использовать либо первый либо второй вариант
    options.add_argument("--headless")
    # options.headless = True
    browser = webdriver.Chrome("D:/chromedriver/chromedriver", options=options)

    try:
        # date_range = pd.date_range(start='02.10.2012', end='02.12.2012', freq='D')
        # вводим период в формате (год, месяц, день)
        date_range = pd.date_range(start=datetime(2020, 6, 24), end=datetime(2020, 6, 25), freq='D')

        start = datetime.strftime(date_range[0], '%d.%m.%Y')
        stop = datetime.strftime(date_range[-1], '%d.%m.%Y')

        data = []
        # проход по всем датам
        for i in date_range:
            date = datetime.strftime(i, '%d.%m.%Y')
            # browser.set_window_size(1920, 1080)
            browser.get(
                f"https://www.stoloto.ru/keno/archive?from={date}&to={date}&firstDraw=1&lastDraw=251057&mode=date")
            time.sleep(random.randrange(1, 2))

            # пытаемся найти кнопку "показать еще" до тех пор пока она есть
            try:
                while True:
                    search_input = browser.find_element('//*[@id="content"]/div[3]/span[1]')
                    search_input.click()
                    print("Прогрузка страницы...")
                    time.sleep(2)
            except:
                print(f'Данные за {date} прогружены')

            # после того как все прогрузилось, собираем нужный нам контент
            page_html = browser.page_source
            soup = BeautifulSoup(page_html, 'html.parser')
            elements = soup.find('div', class_='data drawings_data').find_all('div', class_='elem')
            for element in elements:
                data.append({
                    'date': element.find('div', class_='draw_date').text,
                    'game_n': element.find('div', class_='draw').find('a').text,
                    'numbers': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' '),
                    'payments': element.find('div', class_='prize').get_text(strip=True).replace('\xa0', '')
                })

            print(f'Собранно данных с {len(data)} тиражей')
            # time.sleep(random.randrange(1, 2))

        print(f'Сбор данных тиражей за период с {start} по {stop} завершен.')

        # запись в эксель
        dataframe = pd.DataFrame(data)
        writer = ExcelWriter(f"Результат игр за {start}-{stop}.xlsx")
        dataframe.to_excel(writer, 'data')
        writer.save()
        print(f'Итоговый файл: "Результат игр за {start}-{stop}.xlsx"')

    except Exception as ex:
        print(f'Ошибка: {ex}')
        browser.close()
        browser.quit()
    browser.close()
    browser.quit()


if __name__ == "__main__":
    get_content()
