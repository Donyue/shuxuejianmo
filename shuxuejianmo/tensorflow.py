# -*- conding:utf-8 -*-

# Author : sy

# 下载文件
import wget
import os
os.chdir(r"E:\projects\shuxuejianmo")
url = 'https://raw.githubusercontent.com/wshuyi/demo-customer-churn-ann/master/customer_churn.csv'
filename = wget.detect_filename(url)
wget.download(url)

# 读取数据
import pandas as pd
df = pd.read_csv('customer_churn.csv')
