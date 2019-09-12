# -*- conding:utf-8 -*-

# Author : sy

def k_means(data):
    m = len(data)
    n = len(data[0])
    cluster = [-1 for x in range(k)]    # 所有样本尚未聚类
    cluster_center = [[] for x in range(k)]     # 聚类中心
    cc = [[] for x in range(k)]     # 下一轮的聚类中心
    c_number = [0 for x in range(k)]    # 每个簇中样本的个数

    # 随机选择簇中心
    i = 0
    while i < k:
        j =