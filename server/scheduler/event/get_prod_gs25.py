from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd

def get_prod_gs25(url):
    # selenium driver 설정
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # GS25 행사상품 페이지 접속
    driver.get(url)
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="TOTAL"]'))

    time.sleep(3)
    
    prod_gs25 = pd.DataFrame(columns=['상품명', '가격', '행사유형', '이미지'])
    temp = []

    i = 1
    while i:
        prod_list = driver.find_elements(By.CLASS_NAME, 'prod_list')
        prod_list = prod_list[-1]

        arr = np.array(prod_list.text.split('\n'))
        arr = np.array([str for str in arr if str != ''])
        arr = np.char.replace(arr, '원', '')
        arr = arr.reshape(-1, 3)

        img_url = prod_list.find_elements(By.CSS_SELECTOR, 'li > div > p.img > img')
        img_url = [img.get_attribute('src') for img in img_url]
        img_url = np.array(img_url).reshape(-1, 1)
        arr = np.concatenate((arr, img_url), axis=1)

        if np.array_equal(arr, temp):
            print('end')
            break

        prod_gs25 = pd.concat([prod_gs25, pd.DataFrame(arr, columns=['상품명', '가격', '행사유형', '이미지'])], ignore_index=True)
        temp = arr

        print('crawl page: ', i)
        i += 1

        #href click
        next = driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div[3]/div/div/div[1]/div/a[3]')
        
        driver.execute_script("arguments[0].click();", next)

        time.sleep(2)

    driver.close()

    return prod_gs25