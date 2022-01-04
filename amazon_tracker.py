import requests
from bs4 import BeautifulSoup
from email_alert import alert_system
from threading import Timer

URL = "https://www.amazon.in/Airdopes-121v2-Bluetooth-Immersive-Assistant/dp/B08JQN8DGZ/ref=asc_df_B08JQN8DGZ/?tag=googleshopdes-21&linkCode=df0&hvadid=396987827262&hvpos=&hvnetw=g&hvrand=1752405641764713394&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9075215&hvtargid=pla-1067551499517&psc=1&ext_vrnc=hi"
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

set_price = 1000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    # price = soup.find(id='priceblock_ourprice')
    price = soup.select_one(".a-price .a-offscreen").get_text()

    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) >= set_price:
        alert_system(product_title, URL)
        print('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()

check_price()