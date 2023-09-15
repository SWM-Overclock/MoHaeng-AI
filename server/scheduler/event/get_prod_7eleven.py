from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd

def get_prod_7eleven(url):
    # selenium driver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # 7ELEVEN 행사상품 페이지 접속
    driver.get(url)

    prod_7eleven = pd.DataFrame(columns=['상품명', '가격', '행사유형', '이미지'])

    one_to_one = get_prod(driver)
    prod_7eleven = pd.concat([prod_7eleven, one_to_one], ignore_index=True)

    two_to_one_page = driver.find_element(By.CSS_SELECTOR, '#actFrm > div.cont_body > div.wrap_tab > ul > li:nth-child(2) > a')
    driver.execute_script("arguments[0].click();", two_to_one_page)
    
    two_to_one = get_prod(driver)
    prod_7eleven = pd.concat([prod_7eleven, two_to_one], ignore_index=True)

    print(prod_7eleven)

    return prod_7eleven

def get_prod(driver):
    prod = pd.DataFrame(columns=['상품명', '가격', '행사유형', '이미지'])

    i = 1
    while i:
        try:
            time.sleep(5)
            print('now crawling page: ', i)
            driver.find_element(By.CSS_SELECTOR, '#listUl > li.btn_more > a').click()
            i += 1
        except:
            break

    prodList = driver.find_element(By.CSS_SELECTOR, '#listDiv > div')

    except_list = ['PB', 'MORE', '상품 상세정보 바로가기', '좋아요', ' ', '0', '신상품']
    type_list = ['1+1', '2+1']

    arr = np.array(prodList.get_attribute('innerText').split('\n'))

    arr = np.array([str for str in arr if str not in except_list])
    for el in arr:
        print(el, end=' ')
    print(len(arr))
    arr = arr[1:].reshape(-1, 3) #맨 앞 인덱스 값 제외 ('1+1', '2+1' 등)
    for i in range(len(arr)-1):
        if arr[i][0] not in type_list:
            arr = np.delete(arr, i, axis=0) #잘못된 행 제거 ('이름', '이름', '가격')

    #7ELEVEN 행사상품 이미지가 2개로 나뉘어져 있어서 각각 가져옴
    img_url_top = prodList.find_elements(By.CSS_SELECTOR, 'ul > li > div > img')
    img_url_under = driver.find_elements(By.CSS_SELECTOR, '#listUl > li > div > div > img')
    img_url = img_url_top + img_url_under
    img_url = [img.get_attribute('src') for img in img_url]
    img_url = np.array(img_url).reshape(-1, 1)

    arr = np.concatenate((arr, img_url), axis=1)

    prod = pd.DataFrame(arr, columns=['행사유형', '상품명', '가격', '이미지'])

    return prod