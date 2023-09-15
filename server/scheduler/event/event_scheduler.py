from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np
import pandas as pd
import datetime
from server.scheduler.event.get_prod_gs25 import get_prod_gs25
from server.scheduler.event.get_prod_cu import get_prod_cu
from server.scheduler.event.get_prod_7eleven import get_prod_7eleven
from server.scheduler.event.merge_prod import merge_prod

def crawl_prod():
    prod_gs25 = crawl_prod_gs25()
    prod_cu = crawl_prod_cu()
    prod_7eleven = crawl_prod_7eleven()
    df = merge_prod(prod_7eleven, prod_cu, prod_gs25)

def crawl_prod_gs25():
    get_prod_gs25('http://gs25.gsretail.com/gscvs/ko/products/event-goods')

def crawl_prod_cu():
    get_prod_cu('https://cu.bgfretail.com/event/plus.do')

def crawl_prod_7eleven():
    get_prod_7eleven('http://www.7-eleven.co.kr/product/presentList.asp')