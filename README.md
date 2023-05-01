# 天氣地圖api

## 爬蟲
用sworm.py去獲取opendata的資料
對資料去做處理取的csv檔
更改csv檔的欄位屬性

## 更新資料庫
將獲得的資料更新到資料庫
使用update的方式將新獲取到的表格送到資料庫中

## python flask程式
server.py
建立連線
main.py
主程式，api的設定
目前只有一個request,就是把資料庫的資料回傳出來
models.py
利用models.py格式化好資料庫的資料
並設置好回傳值