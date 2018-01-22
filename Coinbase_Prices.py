#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import datetime
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import csv
from coinbase.wallet.client import *
import sys

# Need to enter new api key and secret 
my_client = Client(api_key="api_key", api_secret="secret", api_version="https://api.coinbase.com/"+datetime.datetime.today().strftime('%Y-%m-%d'))

# Get Datetime info
year = datetime.datetime.now().strftime("%Y")
month = datetime.datetime.now().strftime("%m")
day = datetime.datetime.now().strftime("%d")
hour = datetime.datetime.now().strftime("%H")
minute = datetime.datetime.now().strftime("%M")
second = datetime.datetime.now().strftime("%s")

def get_btcbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = 'BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Buy Price'),buy_price.amount,buy_price.base,buy_price.currency)

def get_btcspot_price(self,currency_pair):
    spot_price = my_client.get_spot_price(currency_pair='BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_btcsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair='BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

def get_ethbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = "ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Buy Price'), buy_price.amount,buy_price.base, buy_price.currency)

def get_ethspot_price(self, currency_pair):
    spot_price = my_client.get_spot_price(currency_pair= "ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_ethsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair ="ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

def get_ltcbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = "LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Buy Price'), buy_price.amount,buy_price.base, buy_price.currency)

def get_ltcspot_price(self, currency_pair):
    spot_price = my_client.get_spot_price(currency_pair= "LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_ltcsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair ="LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(year,month,day,hour,minute,second,str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

f = open('coinbase_prices.csv','a')
f.write('\n'+','.join(get_btcbuy_price(my_client, currency_pair='BTC-USD')))
f.write('\n'+','.join(get_btcspot_price(my_client, currency_pair='BTC-USD')))
f.write('\n'+','.join(get_btcsell_price(my_client, currency_pair='BTC-USD')))
f.write('\n'+','.join(get_ethbuy_price(my_client, currency_pair='ETH-USD')))
f.write('\n'+','.join(get_ethspot_price(my_client, currency_pair='ETH-USD')))
f.write('\n'+','.join(get_ethsell_price(my_client, currency_pair='ETH-USD')))
f.write('\n'+','.join(get_ltcbuy_price(my_client, currency_pair='LTC-USD')))
f.write('\n'+','.join(get_ltcspot_price(my_client, currency_pair='LTC-USD')))
f.write('\n'+','.join(get_ltcsell_price(my_client, currency_pair='LTC-USD')))
f.close()
