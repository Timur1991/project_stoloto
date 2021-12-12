from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import pandas as pd
from datetime import datetime
from pandas import ExcelWriter
#pip install openpyxl

# сделать скроллин страницы чтобы нажать на кнопку "еще"
# сбор архива тиражей игры кено и сохр  в эксель файл


def get_content():
    print('Запуск браузера в фоновом режиме...')
    # browser = webdriver.Chrome('chromedriver/chromedriver')
    options = webdriver.ChromeOptions()
    # добавим свой user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")
    # можно использовать либо первый либо второй вариант
    # options.add_argument("--headless")
    # options.headless = True
    browser = webdriver.Chrome("D:/chromedriver/chromedriver", options=options)

    try:
        # date_range = pd.date_range(start='02.10.2012', end='02.12.2012', freq='D')
        # вводим период в формате (год, месяц, день)
        date_range = pd.date_range(start=datetime(2020, 6, 24), end=datetime(2020, 6, 25), freq='D')
        date_range = pd.date_range(start=datetime(2011, 10, 5), end=datetime(2015, 8, 1), freq='D')

        start = datetime.strftime(date_range[0], '%d.%m.%Y')
        stop = datetime.strftime(date_range[-1], '%d.%m.%Y')

        data = []
        # проход по всем датам
        for i in date_range:
            date = datetime.strftime(i, '%d.%m.%Y')
            # browser.set_window_size(1920, 1080)
            browser.get(
                f"https://www.stoloto.ru/keno/archive?from={date}&to={date}&firstDraw=1&lastDraw=251057&mode=date")
            time.sleep(1)

            # пытаемся найти кнопку "показать еще" до тех пор пока она есть
            try:
                while True:
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    # time.sleep(1)
                    # находим родителя искомого текста
                    xpath = '//span[text()="Показать ещё"]//parent::span'
                    # находим коэфициент на странице
                    show_more = browser.find_element_by_xpath(xpath)
                    print('кликаем по кнопке')
                    show_more.click()
                    print("Прогрузка страницы...")
                    time.sleep(1)
            except:
                print(f'Данные за {date} прогружены')

            # после того как все прогрузилось, собираем нужный нам контент
            page_html = browser.page_source
            soup = BeautifulSoup(page_html, 'html.parser')
            elements = soup.find('div', class_='data drawings_data').find_all('div', class_='elem')
            # print(f'Если тут:{len(elements)} равно 50, то не верно')
            for element in elements:
                data.append({
                    'Дата': element.find('div', class_='draw_date').text.split(' ')[0],
                    'Время': element.find('div', class_='draw_date').text.split(' ')[-1],
                    'Тираж': element.find('div', class_='draw').find('a').text,
                    'Число 1': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[1],
                    'Число 2': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[2],
                    'Число 3': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[3],
                    'Число 4': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[4],
                    'Число 5': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[5],
                    'Число 6': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[6],
                    'Число 7': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[7],
                    'Число 8': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[8],
                    'Число 9': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[9],
                    'Число 10': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[10],
                    'Число 11': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[11],
                    'Число 12': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[12],
                    'Число 13': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[13],
                    'Число 14': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[14],
                    'Число 15': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[15],
                    'Число 16': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[16],
                    'Число 17': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[17],
                    'Число 18': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[18],
                    'Число 19': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[19],
                    'Число 20': element.find('div', class_='container cleared').find('span', class_='zone').text.replace(
                        '\xa0', '').replace('\n', ' ').split(' ')[20],
                    'Выигрыш': element.find('div', class_='prize').get_text(strip=True).replace('\xa0', ''),

                })

            print(f'Собранно данных с {len(data)} тиражей')
            # time.sleep(1)

        print(f'Сбор данных тиражей за период с {start} по {stop} завершен.')

        # запись в эксель
        dataframe = pd.DataFrame(data)
        writer = ExcelWriter(f"Результат игр за {start}-{stop}.xlsx")
        dataframe.to_excel(writer, 'data', index=False)
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
