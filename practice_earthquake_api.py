#利用python網路連線抓取台北市政府公開資料串接
#載入模組
#下載特定網址資料
import urllib.request as req
import json #載入Json模組以獲取Json資料
url="https://dataapi.ncdr.nat.gov.tw/NCDRAPI/Opendata/NCDR/EQ" #最新有感地震資料api
with req.urlopen(url) as res:
  data=json.load(res) #使用json.load取得資料
#print(data) 

#測試列印
#將float轉換成string列印
#info = ["地震名稱:"+eqname, "地震時間:"+eqtime, "地震強度:"+str(eqmag), "地震緯度:"+str(eqlat), "地震經度:"+str(eqlon), "地震深度:"+str(eqdep)+"公里"]

#換行列印
#for x in info:
  #print(x, end = "\n")

#視窗
import tkinter as tk
win=tk.Tk()
win.geometry("800x500")
win.title("即時有感地震顯示器")

#定義變數
titleset = tk.StringVar()
textset = tk.StringVar()
eqname = data["EventName"]
eqtime = data["EventDateTime"]
eqmag = data["Magnitude"]
eqlat = data["EQ_WGS84_Lat"]
eqlon = data["EQ_WGS84_Lon"]
eqdep = data["Depth"]
refreshtext = tk.StringVar()

#標題
title1 = tk.Label(win, textvariable= titleset, fg="black", font=("微軟正黑體", 20))
titleset.set("歡迎來到即時地震資料庫")
title1.place(x = 280, y = 30)

#說明
text1 = tk.Label(win, textvariable= textset, fg="grey", font=("微軟正黑體", 12))
textset.set("資料來源：「交通部中央氣象局」，開放資料即時更新『規模4.0以上』之地震資料")
text1.place(x = 175, y = 60)

#資料顯示
label1 = tk.Label(win, text= "地震名稱：", fg="black", font=("微軟正黑體", 16))
label1.place(x = 290, y = 100)
label1a = tk.Label(win, text = eqname, fg="red", font=("微軟正黑體", 16)) 
label1a.place(x =370, y=100)

label2 = tk.Label(win, text= "地震時間：", fg="black", font=("微軟正黑體", 16))
label2.place(x = 290, y = 130)
label2a = tk.Label(win, text = eqtime, fg="red", font=("微軟正黑體", 16)) 
label2a.place(x =370, y=130)

label3 = tk.Label(win, text= "地震規模：", fg="black", font=("微軟正黑體", 16))
label3.place(x = 290, y = 160)
label3a = tk.Label(win, text = eqmag, fg="red", font=("微軟正黑體", 16)) 
label3a.place(x =370, y=160)
label4b = tk.Label(win, text= "級", fg="black", font=("微軟正黑體", 16))
label4b.place(x = 400, y = 160)

label4 = tk.Label(win, text= "地震緯度：", fg="black", font=("微軟正黑體", 16))
label4.place(x = 290, y = 190)
label4a = tk.Label(win, text = eqlat, fg="red", font=("微軟正黑體", 16)) 
label4a.place(x =370, y=190)
label4b = tk.Label(win, text= "度", fg="black", font=("微軟正黑體", 16))
label4b.place(x = 430, y = 190)

label5 = tk.Label(win, text= "地震經度：", fg="black", font=("微軟正黑體", 16))
label5.place(x = 290, y = 220)
label5a = tk.Label(win, text = eqlon , fg="red", font=("微軟正黑體", 16)) 
label5a.place(x =370, y=220)
label5b = tk.Label(win, text= "度", fg="black", font=("微軟正黑體", 16))
label5b.place(x = 430, y = 220)

label6 = tk.Label(win, text= "地震深度：", fg="black", font=("微軟正黑體", 16))
label6.place(x = 290, y = 250)
label6a = tk.Label(win, text = eqdep, fg="red", font=("微軟正黑體", 16)) 
label6a.place(x =370, y=250)
label6 = tk.Label(win, text= "公里", fg="black", font=("微軟正黑體", 16))
label6.place(x = 410, y = 250)

#更新文字
btntext = tk.Label(win, textvariable= refreshtext, fg="grey", font=("微軟正黑體", 12))
refreshtext.set("點擊按鈕更新資料")
btntext.place(x=340, y= 330)

#時間模組
import time

#按鈕更新
def clickRefresh():
  #重新取樣
  with req.urlopen(url) as res:
    data=json.load(res)

    #現在時間
    now = time.ctime()
    refreshtext.set("資料已更新"+ now) 

#按鈕
btn = tk.Button(win, text = "更新資料", command = clickRefresh)
btn.place(x = 350, y = 300)

win.mainloop()