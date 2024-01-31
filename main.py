from bs4 import BeautifulSoup
import requests
import lxml
import datetime as dt
import http
import smtplib
import time

# Setting the URL of the product we are interested in
URL = "https://www.amazon.com/Fitbit-Advanced-Fitness-Management-PremGear/dp/B0B2222H2R/ref=nav_signin?crid=12JXGZ4MLFULU&keywords=fitbit+5&qid=1704882083&sprefix=fitbit+5%2Caps%2C252&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

# Email credentials
m_email = "costipen57@gmail.com"
password = "gmve lhpl yfic enwb"

# Setting constants
PRICE_POINT = 170
TIME_POINT = "17:33"

# Setting the headers needed in order for Amazon to respond to our GET request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}


def scrape():
    # Launching and storing the Amazon page
    response = requests.get(url=URL, headers=headers)
    amazon = response.text

    soup = BeautifulSoup(amazon, "lxml")

    # Getting the price from the Amazon page and formatting it
    price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
    return price

# Getting the current time and comparing it to the set time
# Comparing the current price of the desired product with the lowest acceptable price
# If the current time matches the set time and the current price is lower than the lowest acceptable price, an email
# notification will be sent to the inputted email address


while True:
    now = dt.datetime.now()
    time_now = str(now).split()[1]
    if time_now[:5] == TIME_POINT:
        current_price = scrape()
        if current_price < PRICE_POINT:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="costipen@yahoo.com",
                    msg=f"Subject:Price Alert\n\nThe product you are targeting is now ${current_price}.\n{URL}"
                )
    time.sleep(60)
