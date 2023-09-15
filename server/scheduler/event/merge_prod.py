import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

def merge_prod(seven_eleven, cu, gs25):
    seven_eleven['편의점'] = '7ELEVEN'
    cu['편의점'] = 'CU'
    gs25['편의점'] = 'GS25'

    df = pd.concat([seven_eleven, cu, gs25])

    today = datetime.today()
    df['시작일'] = datetime(today.year, today.month, 1).strftime('%Y-%m-%d')
    df['종료일'] = (datetime(today.year, today.month, 1) + relativedelta(months=1) - relativedelta(days=1)).strftime('%Y-%m-%d')

    df = pd.DataFrame(df, columns=['편의점', '상품명', '가격', '행사유형', '이미지', '시작일', '종료일'])
    # df.to_csv('product/9월.csv', index=False, encoding='utf-8-sig', columns=['편의점', '상품명', '가격', '행사유형', '이미지'])
    return df