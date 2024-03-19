import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import json

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

try:
    def load_from_json(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    changedList = load_from_json('/Users/jgp/Downloads/data.json')
except:
    changedList = {}


file_name = '나주_전기차충전소정보(결측치제거&읍면동추가분류)'
file_path = f'/Users/jgp/Downloads/{file_name}.csv'

originalColumn = '주소'

data = pd.read_csv(file_path, encoding="utf-8")

driver = webdriver.Chrome()

newAddresses = []
oldAddresses = []
turn = 0

for originalAddress in data[originalColumn]:
    turn = turn + 1

    if originalAddress in changedList:
        oldAddress = changedList[originalAddress]['old']
        newAddress = changedList[originalAddress]['new']
        print(f"({turn}/{len(data[originalColumn])}) {oldAddress}  >>  {newAddress}(이미 변환된 값)")

    else:
        driver.get(f'https://postcode.map.daum.net/search?region_name={originalAddress}&cq={originalAddress}&cpage=1&origin=https%3A%2F%2Fpostcode.map.daum.net&isp=N&isgr=N&isgj=N&ongr=&ongj=&regionid=&regionname=&roadcode=&roadname=&banner=on&ubl=on&indaum=off&vt=layer&amr=on&amj=on&ani=on&mode=view&sd=on&fi=off&fc=on&hmb=off&heb=off&asea=off&smh=off&zo=on&theme=&bit=&sit=&sgit=&sbit=&pit=&mit=&lcit=&plrg=&plrgt=1.5&us=on&msi=10&ahs=off&whas=500&zn=Y&sm=on&CWinWidth=400&sptype=&sporgq=&fullpath=%2Fguide&a51=off')
        time.sleep(1.5)
        try:
            identifier = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dt[1]').text
            if identifier == '지번':
                oldAddress = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button/span[1]').text
                newAddress = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[2]/span[1]/button[1]/span[1]').text
            elif identifier == '도로명':
                newAddress = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button/span[1]').text
                oldAddress = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/ul/li/dl/dd[2]/span[1]/button[1]/span[1]').text
            print(f"({turn}/{len(data[originalColumn])}) {oldAddress}  >>  {newAddress}")
            changedList[originalAddress] = {'new': newAddress, 'old': oldAddress}
        except:
            newAddress = '변환실패'
            oldAddress = '변환실패'
            print(f"({turn}/{len(data[originalColumn])}) {oldAddress}  >>  {newAddress}")
            changedList[originalAddress] = {'new': newAddress, 'old': oldAddress}

        save_to_json(changedList, '/Users/jgp/Downloads/data.json')



    oldAddresses.append(oldAddress)
    newAddresses.append(newAddress)

data['지번주소'] = oldAddresses
data['도로명주소'] = newAddresses

driver.quit()  # 웹 드라이버 종료

# 저장된 새로운 열을 확인합니다.
print(data.head())

# 다시 csv 파일로 저장
data.to_csv(f'/Users/jgp/Downloads/{file_name}_변환완료.csv', index=False, encoding="cp949")
