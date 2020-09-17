import requests
import time
from datetime import datetime
IFTTT_WEBHOOKS_URL = "https://maker.ifttt.com/trigger/{}/with/key/clDkQIKhSaD3W5nZTcYib3"
BITCOIN_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
def get_latest_bitcoin_price() :
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()
    BITCOIN_PRICE = response_json["bpi"]['USD']['rate']
    BITCOIN_PRICE = BITCOIN_PRICE.replace(",", "")
    return float(BITCOIN_PRICE)
def post_ifttt_webhook(event, value) :
    data = {'value1' : value}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json = data)
BITCOIN_PRICE_THRESHOLD = 1000000000000000
def format_bitcoin_history(bitcoin_history) :
    rows = []
    for bitcoin_price in bitcoin_history :
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)
    return '<br>'.join(rows)
def main() :
    print("WELCOME TO BITCOIN PRICE NOTIFICATION")
    bitcoin_history = []
    while True :
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})
        if price < BITCOIN_PRICE_THRESHOLD :
            post_ifttt_webhook("bitcoin_price_emergency", price)
        if len(bitcoin_history) == 5 :
            post_ifttt_webhook('Bitcoin_price_update',format_bitcoin_history(bitcoin_history))
            bitcoin_history = []
        time.sleep(3)
        print("DO YOU WANT TO EXIT")
        user_input = input("Enter yes or no :\n")
        if user_input == "yes" :
            return
        else:
            continue    

if __name__ == "__main__":
    main()

