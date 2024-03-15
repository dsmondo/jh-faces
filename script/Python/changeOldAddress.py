import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

file_path = '/Users/jgp/Downloads/전라남도_나주시_주유소및LPG충전소_20230104.csv'

data = pd.read_csv(file_path, encoding='cp949')

driver = webdriver.Chrome()

new_addresses = []
turn = 0

for address in data['소재지지번주소']:
    turn = turn + 1
    driver.get(f'https://postcode.map.daum.net/search?region_name={address}&cq={address}&cpage=1&origin=https%3A%2F%2Fpostcode.map.daum.net&isp=N&isgr=N&isgj=N&ongr=&ongj=&regionid=&regionname=&roadcode=&roadname=&banner=on&ubl=on&indaum=off&vt=layer&amr=on&amj=on&ani=on&mode=view&sd=on&fi=off&fc=on&hmb=off&heb=off&asea=off&smh=off&zo=on&theme=&bit=&sit=&sgit=&sbit=&pit=&mit=&lcit=&plrg=&plrgt=1.5&us=on&msi=10&ahs=off&whas=500&zn=Y&sm=on&CWinWidth=400&sptype=&sporgq=&fullpath=%2Fguide&a51=off')
    time.sleep(1.5)
    new_address_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[2]/span[1]/button[1]/span[1]')
    new_address = new_address_element.text.strip() if new_address_element else ""
    if not new_address:
        time.sleep(2)
        new_address_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[2]/span[1]/button[1]/span[1]')
        new_address = new_address_element.text.strip() if new_address_element else ""
    print(f"({turn}/{len(data['소재지지번주소'])}) {address}  >>  {new_address}")
    new_addresses.append(new_address)

data['new_address'] = new_addresses

driver.quit()  # 웹 드라이버 종료

# 저장된 새로운 열을 확인합니다.
print(data.head())

# 필요하면 새로운 주소를 저장한 데이터프레임을 다시 csv 파일로 저장할 수 있습니다.
data.to_csv('/Users/jgp/Downloads/전라남도_나주시_주유소및LPG충전소_20230104_new2.csv', index=False, encoding='cp949')
