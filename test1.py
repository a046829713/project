import csv



with open('new_data.csv',newline='',encoding='utf-8-sig') as csvfile:
    data1 = csv.reader(csvfile)
    data1 = [i[0] for i in data1]
    
    
with open('盤點資料.csv',newline='',encoding='utf-8-sig') as csvfile:
    data2 = csv.DictReader(csvfile)       
    out_data2 = [i['trl_ID'] for i in data2]
    



#將兩者合併
out_dict ={}

for i in data1:
    if i in out_dict:
        out_dict[i] +=1
    else:
        out_dict[i] = 1
        
for i in out_data2:
    if i in out_dict:
        out_dict[i] +=1
    else:
        out_dict[i]  = 1
        



# 開啟輸出的 CSV 檔案
with open('清理後盤點資料.csv', 'w', newline='',encoding='utf-8') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerow(['TRL_ID','盤點日期'])
    for i in list(out_dict.keys()):
        # 寫入一列資料
        writer.writerow([i])