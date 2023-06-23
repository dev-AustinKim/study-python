import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\gb_0900_kdh\python\네이버 주식 현재가 크롤링\주식가_data.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택


# 종목 코드 리스트
codes = [
    '030200',
    '066570',
    '005930'
]

row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace("," , "")
    print(price)
    ws[f'B{row}'] = int(price)
    row = row + 1

wb.save(fpath)