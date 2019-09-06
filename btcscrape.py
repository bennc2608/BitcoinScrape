if __name__ == '__main__':
    main()
def main():
    '''
    My main btc scrape
    '''
    from urllib import request
    import json
    from datetime import datetime
    import sqlite3
    import time

    url = 'https://api.coindesk.com/v1/bpi/currentprice/GBP.json'
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    conn = sqlite3.connect(r'C:\Projects\bitcoinscrape\crypto')
    c = conn.cursor()
    while True:
        
        req = request.Request(url,header=header)
        with request.urlopen(req) as data:
            jsondata = json.load
        dt = datetime.strptime(jdata['time']['updateduk'], '%b %d, %Y at %H:%M BST')
        rate = jdata['bpi']['GBP']['rate_float']
        param = (dt, 'GBP', rate)
        c.execute('insert into BTC (pricedate, currency, rate) values (?, ?, ?)', param)
        conn.commit()
        time.sleep(60)
    
