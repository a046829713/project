import csv

with open('20221111平面資料.csv',newline='',encoding='utf-8-sig') as csvfile:
    data1 = csv.DictReader(csvfile)
    for i in data1:
        print(i)