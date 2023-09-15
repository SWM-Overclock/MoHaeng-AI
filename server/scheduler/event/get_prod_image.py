import pandas as pd
import urllib.request
import shutil
from datetime import datetime

def get_prod_images(df, shop):
    month = datetime.today().month
    src = f'product/images/{shop}_준비중.png'
    for i in range(len(df)):
        print('now downloading image: ', i)
        try:
            urllib.request.urlretrieve(df['이미지'][i], f'product/images/{month}/{shop}/{str(i)}.jpg')
        except:
            print('failed: ', i)
            shutil.copy(src, f'product/images/{month}/{shop}/{str(i)}.jpg')
