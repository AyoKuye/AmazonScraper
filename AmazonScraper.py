import requests
from bs4 import BeautifulSoup
import smtplib
import time

#Insert URL
URL = 'https://www.amazon.com/Nintendo-Console-Resolution-802-11ac-Surround/dp/B07RGFF98S/ref=sr_1_5?dchild=1&keywords=nintendo+switch&qid=1595052854&s=electronics&sr=1-5'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

#Checks if Price Dropped
def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if(converted_price < 320):
        send_mail()

    print(converted_price)
    print(title.strip())
    
    if(converted_price < 320):
        send_mail()


#Sends Email after Drop in Price
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ayokuye23@gmail.com', 'gdgofktqlvenybho')

    subject = 'Price Drop!'
    body = 'Check the Link, the price finally dropped https://www.amazon.com/Nintendo-Console-Resolution-802-11ac-Surround/dp/B07RGFF98S/ref=sr_1_5?dchild=1&keywords=nintendo+switch&qid=1595052854&s=electronics&sr=1-5'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ayokuye23@gmail.com',
        'ayokuye13@gmail.com',
        msg
    )

    print('Email has been sent'
    
    )

    server.quit

#Program runs once a day
while(True):
    check_price()
    time.sleep(60 * 1440)
