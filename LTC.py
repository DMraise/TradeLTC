import ccxt
import sqlite3
import pandas as pd
import time
import re
# exchange = ccxt.kucoin({
#     'enbaleRateLimit': True,
#     'api_key': '64a2ac31cb1cfe000170fabe',
#     'secret': '941fc9c2-7bb0-4a2c-b83c-954e7fcf773f',
#     'password': 'CODDICODDICODi1'
# })
exchange = ccxt.okx({
    'enbaleRateLimit': True,
    'api_key': 'eaf82e24-0798-4351-b86d-4282e276870f',
    'secret': 'FC7365A045EB8085565C3A7966CA0F44',
    'password': 'CODDICODDICODi1!'

})
def is_exponential(num):
        pattern = r'^[-+]?[0-9]+(\.[0-9]+)?[eE][-+]?[0-9]+$'
        return bool(re.match(pattern, str(num)))
              
def get_USDT():
    balance = exchange.fetch_balance()
    return balance['total']['USDT']

balances = exchange.fetch_balance()
a = balances['total']['USDT']
print(a)

def get_OKB():
    balance = exchange.fetch_balance()
    if is_exponential(balance['total']['OKB']) == True:
        balance = '{:0.9f}'.format(balance['total']['OKB'])
        return balance
    else:
        return balance['total']['OKB']

def get_XRP():
        balance = exchange.fetch_balance()
        if is_exponential(balance['total']['XRP']) == True:
            balance = '{:0.9f}'.format(balance['total']['XRP'])
            return balance
        else:
            return balance['total']['XRP']
            
def get_ETH():
        balance = exchange.fetch_balance()
        if is_exponential(balance['total']['ETH']) == True:
            balance = '{:0.9f}'.format(balance['total']['ETH'])
            return balance
        else:
            return balance['total']['ETH']
        
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

start_USD = get_USDT()
USDT = exchange.fetch_ticker('OKB/USDT')
print(USDT)
USDT = USDT['bid']
print("USDT: ", get_USDT())
print("Цена OKB/USDT: ", USDT)
print("Обмен USDT на OKB Количество OKB: ", get_USDT()/USDT)
OKB = get_USDT()/USDT

USDT1 = exchange.fetch_ticker('XRP/OKB')
print(USDT1)
USDT1 = USDT1['bid']
print("Цена XRP/OKB: ", USDT1)
print("Обмен OKB на XRP Количество XRP: ", OKB/USDT1)
XRP = OKB/USDT1

USDT2 = exchange.fetch_ticker('XRP/ETH')
print(USDT2)
USDT2 = USDT2['bid']
print("Цена XRP/ETH: ", USDT2)
print("Обмен XRP на ETH Количество ETH: ", XRP*USDT2)
ETH = XRP*USDT2

USDT3 = exchange.fetch_ticker('ETH/USDT')
print(USDT3)
USDT3 = USDT3['bid']
print("Цена ETH/USDT: ", USDT3)
print("Обмен ETH на USDT Количество USDT: ", ETH*USDT3)
end_USD = ETH*USDT3
print("Итоговая сумма: ", end_USD - start_USD)

while True:
    USDT = exchange.fetch_ticker('OKB/USDT')
    USDT = USDT['bid']

    USDT1 = exchange.fetch_ticker('XRP/OKB')
    USDT1 = USDT1['bid']

    USDT2 = exchange.fetch_ticker('XRP/ETH')
    USDT2 = USDT2['bid']

    USDT3 = exchange.fetch_ticker('ETH/USDT')
    USDT3= USDT3['bid']
    start_U = get_USDT()
    OKB = get_USDT()/USDT

    XRP = OKB/USDT1

    ETH = XRP*USDT2
    USD = ETH*USDT3
    end = USD - start_U 
    print("Итоговая сумма в USDT: ", USD, "Разница: ", end)
    if end >= 0.08:
        print("БОЛЬШАЯ СУММА!", end)
        balance_USDT = get_USDT()
        try:
            print("Баланс USDT:", balance_USDT)

            order = exchange.create_order(symbol='OKB/USDT', type='market', side='buy',  amount=float(get_USDT()))

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        print(get_OKB())
        balance_OKB = get_OKB()
        try:
            print("Баланс OKB: ", balance_OKB)
            amount = get_OKB()/USDT1
            order = exchange.create_order(symbol='XRP/OKB', type='market', side='buy',  amount=amount)

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        balance_XRP = get_XRP()
        try:
            print("Баланс XRP:", balance_XRP)
            amount = get_XRP()*USDT2
            order = exchange.create_order(symbol='XRP/ETH', type='market', side='sell',  amount=get_XRP())

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        balance_ETH = get_ETH()
        try:
            print("Баланс ETH: ", balance_ETH)
            amount = float(get_ETH())*float(USDT3)
            order = exchange.create_order(symbol='ETH/USDT', type='market', side='sell',  amount=get_ETH())

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))

    time.sleep(1)

