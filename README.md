# 加密樂透
用加密貨幣買樂透吧！
- 利用python flask + SQLite +ngrok簡單架設一個Linebot


## 需求
- 開發者需事先準備line developer的帳號，取得token與key才能使用
- 需自行在環境中使用ngrok讓外網可連接到API

## 功能
- 顯示比特幣價格
- 下單購買樂透（目前只有隨機選號）
- 顯示擁有的彩券
- 顯示當期樂透號碼（顯示當期台彩彩券號碼，因故未實作)

## 功能展示

### Linebot首頁
![image](https://github.com/Alan-Cheng/lottery_project/blob/main/DEMO/linebot.png)

### 幣價查詢功能
- Bitcoin price來自 Coinbase API
![image](https://github.com/Alan-Cheng/lottery_project/blob/main/DEMO/show_price.jpg)

### 下注功能
- 目前只提供自動選號下注，但可以選擇換號
- 確認選號後會要求匯款與提供匯款人錢包地址
- 收發幣只接受P2SH格式(有格式確認機制)
![image](https://github.com/Alan-Cheng/lottery_project/blob/main/DEMO/bet.jpg)
