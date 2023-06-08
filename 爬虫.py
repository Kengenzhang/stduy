import re

import requests
import csv

def my_replace(str_):
    return str_.replace('<div class="td-wrap"><div class="td-wrap-in">', '').replace('</div></div>', '')
    
with open('rank.csv',mode='a',encoding='utf-8',newline='') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['country', 'rank', 'region', 'score_1', 'score_2', 'score_4', 'score_5', 'score_6', 'score_7', 'score_8','university'])


# 找数据来源
ulr = 'https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2174878_indicators.txt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
# 发送数据请求
repose = requests.get(url=ulr, headers=headers)
# print(repose)
# 获取数据
json_data = repose.json()
list_ = json_data['data']
for li in list_:
    country = li['location']  # 国家
    rank = li['overall_rank']  # 排名
    region =li['region']  # 地区
    score_1 = my_replace(li['overall'])  # 综合得分
    score_2 = my_replace(li['ind_76'])  # 学术声誉
    score_4 = my_replace(li['ind_77']) # 雇主声誉
    score_5 = my_replace(li['ind_73'])  # 每位教员引用率
    score_6 = my_replace(li['ind_36'])  # 师生比
    score_7 = my_replace(li['ind_14'])  # 国际学生占比
    score_8 = my_replace(li['ind_18'])  # 国际教师占比
    university_=my_replace(li['uni'])    #大学名称
    university=re.findall('<a href="/universities/.*?>(.*?)</a>',university_)[0]
    with open('rank.csv',mode='a',encoding='utf-8',newline='') as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([country, rank, region, score_1, score_2, score_4, score_5, score_6, score_7, score_8,university])

