import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

re = requests.get('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
res = re.content

soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())

price = float(soup.find('p', class_='price_color').text[1:])
# print(type(price))

if price < 60:
    smt = smtplib.SMTP('smtp.gmail.com',587)
    smt.ehlo()
    smt.starttls()
    smt.login('mokuasamr@gmail.com',os.environ.get('APP_PASSWORD'))
    smt.sendmail('mokuasamr@gmail.com',
                'rasuguofficial@gmail.com', 
                f'Subject: Price Drop\n\nThe price of the book has dropped to {price}'
                )
    smt.quit()