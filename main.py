import ccxt
import sqlite3
import pandas as pd
import time
exchange = ccxt.kucoin({
    'enbaleRateLimit': True,
    'api_key': '64a2ac31cb1cfe000170fabe',
    'secret': '941fc9c2-7bb0-4a2c-b83c-954e7fcf773f',
    'password': 'CODDICODDICODi1'
})
#print(phemex.fetch_balance())
#a = phemex.market('ETH/EUR') 
# #print(a)
# def function_price():
#     ap = []
#     #tikers = ['BTC/EURT', 'BTC/USDC', 'BTC/DAI']
#    # tiker_1 = ['BTC/EURT', 'BTC/USDC', 'BTC/DAI']
#     tikers = ['LTC/KCS', 'LTC/ETH', 'LTC/USDC', 'LTC/KCS', 'LTC/USDT']
#     tiker_1 = ['LTC/KCS', 'LTC/ETH', 'LTC/USDC', 'LTC/KCS', 'LTC/USDT']
#     app = []
#     while True:
#         app.clear()
#         ap.clear()
#         for i in tikers:
#             symbola = exchange.fetch_ticker(i)
#             symbola = symbola['bid']
#             for j in tiker_1:
#                 symbolb = exchange.fetch_ticker(j)
#                 symbolb = symbolb['bid']
#                 res = ((symbola-symbolb)/symbola)*100
#                 x = round(res, 2)
#                 app.append(x)
#     #    df = pd.DataFrame({'name': ['BTC/USDT', 'BTC/TUSD', 'BTC/USDC', 'BTC/DAI'], 'a': [1, 0,2,3]})
#         print(app)
#         time.sleep(1)

#     print(df)
#     print(ap)
# spisok = ['XRP/USDT', 'XRP/TUSD', 'XRP/USDC', 'XRP/ETH', 'XRP/BTC', 'XRP/KCS']
# for i in spisok:
#     if i == i:
#         continue
#     else:
#         pass
#         print(i)

def get_USDT():
    balance = exchange.fetch_balance()
    return balance['USDT']['free']

def get_TUSD():
    balance = exchange.fetch_balance()
    b = balance['info']['data']
    print(b)
    for i in range(len(b[0])):
        a = b[i]
        print(a)
        if a['currency'] == 'TUSD':
            ret = b[i]['balance']
            return ret
        break

print(get_TUSD())
def get_XRP():
        balance = exchange.fetch_balance()
        b = balance['info']['data']
        for i in range(len(b[0])):
            a = b[i]
            if a['currency'] == 'XRP':
                ret = b[i]['balance']
                return ret
            break
print(get_XRP())    
def get_KCS():
        balance = exchange.fetch_balance()
        b = balance['info']['data']
        for i in range(len(b[0])):
            a = b[i]
            if a['currency'] == 'KCS':
                ret = b[i]['balance']
                return ret
            break
print(get_KCS())
        
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

while True:
    USDT = exchange.fetch_ticker('USDT/TUSD')
    USDT = USDT['bid']
    #USDT = float('{:.3f}'.format(USDT))
   # print("Цена USDT к TUSD: ", USDT)

    USDT1 = exchange.fetch_ticker('XRP/TUSD')
    USDT1 = USDT1['bid']
    #USDT1 = float('{:.5f}'.format(USDT1))
   # print("Цена XRP к TUSD: ", USDT1)

    USDT2 = exchange.fetch_ticker('XRP/KCS')
    USDT2 = USDT2['bid']
    #USDT2 = float('{:.5f}'.format(USDT1))
   # print(USDT2)

    USDT3 = exchange.fetch_ticker('KCS/USDT')
    USDT3= USDT3['bid']

   # print("Цена Биткоина к Доллару:", USDT3)

    USDT_LTC = 10*USDT

    #res1 = float('{:.5f}'.format(USDT_LTC))
   # print("Перевод USDT в LTC: ", USDT_LTC)

    LTC_BTC = USDT_LTC/USDT1
    #res2 = float('{:.5f}'.format(USDT_LTC))
   # print("Перевод LTC в BTC: ", LTC_BTC)

    resff = LTC_BTC*USDT2
    res3 = resff*USDT3

    print("Итоговая сумма в USDT: ", res3)
    if res3 >= 10.05:
        print("БОЛЬШАЯ СУММА!", res3)
        balance_USDT = get_USDT()
        try:
            amount = float(balance_USDT)/float(USDT)

            order = exchange.create_order(symbol='USDT/TUSD', type='marker',  side='sell',  amount=amount)

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        time.sleep(0.2)
        balance_TUSD = get_TUSD()
        try:
            amount = float(balance_TUSD)/float(USDT1)
            order = exchange.create_order(symbol='XRP/TUSD', type='marker', side='buy',  amount=amount)

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        time.sleep(0.2)
        balance_XRP = get_XRP()
        try:
            amount = float(balance_XRP)
            order = exchange.create_order(symbol='XRP/KCS', type='marker', side='sell',  amount=amount)

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))
        time.sleep(0.2)
        balance_KCS = get_KCS()
        try:
            amount = float(balance_KCS)
            order = exchange.create_order(symbol='KCS/USDT', type='marker', side='sell',  amount=amount)

            print('Ордер успешно размещен:', order)
        except ccxt.BaseError as e:
            print('Произошла ошибка при размещении ордера:', str(e))

    time.sleep(1)

