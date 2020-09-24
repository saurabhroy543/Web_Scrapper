import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07X9YMW7S/ref=sr_1_1_sspa?dchild=1&keywords=samsung+m51&qid=1600070233&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNjNXT0VaUUY4UUJKJmVuY3J5cHRlZElkPUEwNjkwNDA5MjhXUVpXSE9CTzZVRSZlbmNyeXB0ZWRBZElkPUEwMDI2MTAyMURES0hSR1g0UUEzTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettiffy())
