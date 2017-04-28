## -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np

#分析網址
url = "http://www.gu-global.com/tw/store/feature/gu/women/limited/"
price_list = []

#BeautifulSoup可以拿來parsing(語法分析) html的內容，並擷取你想要的tag以及content資料
soup = BeautifulSoup(requests.get(url).text, 'html5lib')


for div in soup('div',"unit"):
    #查詢<dt class="name"> 抓取商品名稱
    title = div.find("dt","name").text.strip().split('\t')[-1]
    #查詢<dd class="price"> 抓取商品價格
    price = div.find("dd", "price").text.strip()
    #取$後的價錢 price_list
    price_list.append(int(price.split('$')[-1]))

    print title , "價格 :" ,price


#print price_list
#計算價格層別的個數
price_count =[0,0,0,0,0,0,0,0,0,0,0]
price_level = ['100','200','300','400','500','600','700','800','900','1000','1000~']

for i in price_list:
   if i > 1000:
       price_count [10] += 1
   elif i >900 :
      price_count[9] += 1
   elif i >800:
      price_count[8]+= 1
   elif i > 700:
      price_count[7] += 1
   elif i > 600:
      price_count[6] += 1
   elif i > 500:
      price_count[5] += 1
   elif i > 400:
      price_count[4] += 1
   elif i > 300:
      price_count[3] += 1
   elif i > 200:
      price_count[2] += 1
   elif i > 100 :
      price_count[1] += 1
   else :
       price_count[0] +=1

x = np.array([0,1,2,3,4,5,6,7,8,9,10,])
plt.xticks(x, price_level)
plt.plot(x,price_count)
plt.ylabel("price of data")
plt.xlabel("price level")
plt.title("Price distribution")
plt.show()


