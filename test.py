import csv



data1 =[]
# 開啟 CSV 檔案
with open('盤點資料-手.csv', newline='',encoding='utf-8-sig') as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈輸出每一列
    data1 = [row[0] for row in rows]
        

data2 =[]
# 開啟 CSV 檔案
with open('5F.csv', newline='',encoding='utf-8-sig') as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    
    # 以迴圈輸出每一列
    data2 = [row[0] for row in rows]
    


out_dict = {}
for i in data1:
    if i in out_dict:
        out_dict[i] +=1
    else:
        out_dict[i] = 1
        
        
for i in data2:
    if i in out_dict:
        out_dict[i] +=1
    else:
        out_dict[i] = 1
        


# 開啟輸出的 CSV 檔案
with open('new_data.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    for i in list(out_dict.keys()):
        # 寫入一列資料
        writer.writerow([i])

