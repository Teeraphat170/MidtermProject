CP353Project_midterm
ชื่อสมาชิกในกลุ่ม

นาย ธนกร สุจิรภิญโญกุล
นาย ธนพัฒน์ เอี่ยมประเสริฐ
นาย ศรายุธ ธนาคำ
สิ่งที่ต้องทำการรันโปรแกรม

เปิด Environment > Environment variables > New ที่ User variable for ...

สมัคร API KEY จาก https://www.api-football.com/

Variables name = FOOTBALL_API_KEY

Variables value = APIKEY จาก https://www.api-football.com/

สมัคร API KEY จาก https://rapidapi.com/datascraper/api/livescore-football

Variables name = NEWS_API_KEY

Variables value = APIKEY จาก https://rapidapi.com/datascraper/api/livescore-football

วิธีรันโปรแกรม

ติดตั้ง python
เปิด cmd และติดตั้งmodule pip install
มี module ดังนี้
flask
flask_sqlalchemy
MarkupSafe
OS
ให้เข้าที่ path เดียวกับ app.py
$env:FLASK_APP="app.py"
flask run