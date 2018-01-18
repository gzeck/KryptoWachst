#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import datetime
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import csv
from coinbase.wallet.client import *
import sys

# api_key = "7HpV5wN4mthzyhtT"
# api_secret = "NrEB9mCSIstEyAYyzs6IBah8yION4GI7"
#CB_VERSION = '2018-01-13'
my_client = Client(api_key="7HpV5wN4mthzyhtT", api_secret="NrEB9mCSIstEyAYyzs6IBah8yION4GI7", api_version="https://api.coinbase.com/"+'"2018-01-13')

def get_btcbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = 'BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(timestamp,str('Buy Price'), buy_price.amount,buy_price.base, buy_price.currency)

def get_btcspot_price(self,currency_pair):
    spot_price = my_client.get_spot_price(currency_pair='BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(timestamp, str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_btcsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair='BTC-USD')
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(timestamp, str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

def get_ethbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = "ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(timestamp,str('Buy Price'), buy_price.amount,buy_price.base, buy_price.currency)

def get_ethspot_price(self, currency_pair):
    spot_price = my_client.get_spot_price(currency_pair= "ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(timestamp, str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_ethsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair ="ETH-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(timestamp, str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

def get_ltcbuy_price(self, currency_pair):
    buy_price = my_client.get_buy_price(currency_pair = "LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Buy Price: $%s : Timestamp: %s" % (buy_price.amount, timestamp)
    return(timestamp,str('Buy Price'), buy_price.amount,buy_price.base, buy_price.currency)

def get_ltcspot_price(self, currency_pair):
    spot_price = my_client.get_spot_price(currency_pair= "LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Spot Price: $%s : Timestamp: %s" %(spot_price.amount, timestamp)
    return(timestamp, str('Spot Price'), spot_price.amount,spot_price.base, spot_price.currency)

def get_ltcsell_price(self, currency_pair):
    sell_price = my_client.get_sell_price(currency_pair ="LTC-USD")
    timestamp = datetime.datetime.now()
    #price_stamp = "Sell Price: $%s : Timestamp: %s" %(sell_price.amount, timestamp)
    return(timestamp, str('Sell Price'),sell_price.amount,sell_price.base, sell_price.currency)

f = open('coinbase_prices.csv','a')
f.write(str(get_btcbuy_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_btcspot_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_btcsell_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ethbuy_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ethspot_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ethsell_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ltcbuy_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ltcspot_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.write(str(get_ltcsell_price(my_client, currency_pair='BTC-USD'))+ '\n')
f.close()
