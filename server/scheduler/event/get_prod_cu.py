from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd

def get_prod_cu(url):
    # selenium driver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # CU 행사상품 페이지 접속
    driver.get(url)

    i = 1
    while i:
        try:
            time.sleep(7)
            print('now crawling page: ', i)
            driver.find_element(By.CSS_SELECTOR, '#contents > div.relCon > div > div > div.prodListBtn-w > a').click()
            i += 1
        except:
            break

    prod_cu = pd.DataFrame(columns=['상품명', '가격', '행사유형', '이미지'])

    allProdListWrap = driver.find_elements(By.CSS_SELECTOR, '#contents > div.relCon > div > ul')

    for prodListWrap in allProdListWrap:
        arr = np.array(prodListWrap.get_attribute('innerText').split('\n'))
        arr = np.array([str for str in arr if str != '' and str != '원'])
        arr = arr.reshape(-1, 3)

        img_url = prodListWrap.find_elements(By.CLASS_NAME, 'prod_img')
        img_url = [img.get_attribute('src') for img in img_url]
        img_url = [img for img in img_url if img != None]
        img_url = np.array(img_url).reshape(-1, 1)

        arr = np.concatenate((arr, img_url), axis=1)

        prod_cu = pd.concat([prod_cu, pd.DataFrame(arr, columns=['상품명', '가격', '행사유형', '이미지'])], ignore_index=True)

    return prod_cu