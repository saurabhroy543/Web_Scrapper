
import smtplib
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07X9YMW7S/ref=sr_1_1_sspa?dchild=1&keywords=samsung+m51&qid=1600070233&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNjNXT0VaUUY4UUJKJmVuY3J5cHRlZElkPUEwNjkwNDA5MjhXUVpXSE9CTzZVRSZlbmNyeXB0ZWRBZElkPUEwMDI2MTAyMURES0hSR1g0UUEzTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
 


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()


    new_price=(price[2:8])

    print(price[2:8])
    print(title.strip())

    if new_price> '20,000':
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('saurabhr543@gmail.com','slhlobpcjlrnggac')

    subject = 'price fell down'

    body = 'check out the price link https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07X9YMW7S/ref=sr_1_1_sspa?dchild=1&keywords=samsung+m51&qid=1600070233&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNjNXT0VaUUY4UUJKJmVuY3J5cHRlZElkPUEwNjkwNDA5MjhXUVpXSE9CTzZVRSZlbmNyeXB0ZWRBZElkPUEwMDI2MTAyMURES0hSR1g0UUEzTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
 
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'saurabhr543@gmail.com',
        'shubo98521 @gmail.com',
        msg
        )

    print('mail sent')
    server.quit()



