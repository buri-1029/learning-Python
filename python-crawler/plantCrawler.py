import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 프로젝트에 필요한 식물 정보 크롤링
csv_name = "code.csv"
csv_open = open(csv_name, "w+", encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('name'))

# csv_name = "plantInfo.csv"
# csv_open = open(csv_name, "w+", encoding='utf-8')
# csv_writer = csv.writer(csv_open)
# csv_writer.writerow(('common_name', 'name', 'category', 'level',
#                     'water', 'humid', 'temp', 'language', 'info', 'image'))

driver = webdriver.Chrome(ChromeDriverManager().install())

pages = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
         "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]

for page in pages:
    driver.get(
        "http://api.nongsaro.go.kr/sample/rest/garden/gardenList.jsp?cntntsNo=&pageNo="+page)
    html = driver.page_source  # html을 문자열로 가져온다.
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(3)

    infos = soup.select('body > table > tbody > tr > td > a')

    for i in infos:
        name = i.text
        print(name)
        csv_writer.writerow([name])

# for code in codes:
#     driver.get(
#         "http://api.nongsaro.go.kr/sample/rest/garden/gardenDtl.jsp?cntntsNo="+code)
#     html = driver.page_source  # html을 문자열로 가져온다.
#     soup = BeautifulSoup(html, 'html.parser')

#     time.sleep(3)

#     infos = soup.select('body > table > tbody > tr')

#     info_list = []

#     for i in infos:
#         info = i.find('td').text
#         info_list.append(info)
#         print(info)

#     csv_writer.writerow(info_list)
