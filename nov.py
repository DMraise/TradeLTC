import ccxt
import time
import re

exchange = ccxt.okx({
    'enbaleRateLimit': False,
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
  
def get_balance(monet):
    balance = exchange.fetch_balance()
    if is_exponential(balance['total'][monet]) == True:
        balance = '{:0.9f}'.format(balance['total'][monet])
        print("Возвращаю переведенне значенение", balance)
        return balance
    else:
        print("Возвращаю непереведенное значение", balance['total'][monet])
        return balance['total'][monet]
max_price = 0
pair1 = ''
pair2 = ''

def pairs():
    def pair11():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/USDC')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/ETH')
        b = b['bid']
        c = exchange.fetch_ticker('USDC/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('ETH/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/USDC'
            pair2 = 'XRP/ETH'
        print(f"Изменение в цене: {end}")
    pair11()
    def pair22():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/USDC')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/BTC')
        b = b['bid']
        if is_exponential(b) == True:
            balance = '{:0.9f}'.format(b)
            b = float(balance)
        c = exchange.fetch_ticker('USDC/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('BTC/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/USDC'
            pair2 = 'XRP/BTC'
        print(f"Изменение в цене: {end}")
    pair22()
    def pair3():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/USDC')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/OKB')
        b = b['bid']
        c = exchange.fetch_ticker('USDC/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('OKB/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/USDC'
            pair2 = 'XRP/OKB'
        print(f"Изменение в цене: {end}")
    pair3()
    def pair4():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/USDC')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/USDT')
        b = b['bid']
        c = exchange.fetch_ticker('USDC/USDT')
        c = c['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        end = step3-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/USDC'
            pair2 = 'XRP/USDT'
        print(f"Изменение в цене: {end}")
    # pair4()
    def pair5():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/ETH')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/USDC')
        b = b['bid']
        c = exchange.fetch_ticker('ETH/USDT')
        c = c['bid']
        if is_exponential(c) == True:
            balance = '{:0.9f}'.format(c)
            c = float(balance)
        d = exchange.fetch_ticker('USDC/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/ETH'
            pair2 = 'XRP/USDC'
        print(f"Изменение в цене: {end}")
    pair5()
    def pair6():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/ETH')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/BTC')
        b = b['bid']
        if is_exponential(b) == True:
            balance = '{:0.9f}'.format(b)
            b = float(balance)
        c = exchange.fetch_ticker('ETH/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('BTC/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/ETH'
            pair2 = 'XRP/BTC'
        print(f"Изменение в цене: {end}")
    pair6()
    def pair7():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/ETH')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/OKB')
        b = b['bid']
        c = exchange.fetch_ticker('ETH/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('OKB/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/ETH'
            pair2 = 'XRP/OKB'
        print(f"Изменение в цене: {end}")
    pair7()
    def pair8():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/ETH')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/USDT')
        b = b['bid']
        c = exchange.fetch_ticker('ETH/USDT')
        c = c['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        end = step3-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/ETH'
            pair2 = 'XRP/USDT'
        print(f"Изменение в цене: {end}")
    pair8()
    def pair9():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/OKB')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/USDC')
        b = b['bid']
        c = exchange.fetch_ticker('OKB/USDT')
        c = c['bid']
        d = exchange.fetch_ticker('USDC/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/OKB'
            pair2 = 'XRP/USDC'
        print(f"Изменение в цене: {end}")
    pair9()
    def pair10():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/OKB')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/ETH')
        b = b['bid']
        if is_exponential(b) == True:
            balance = '{:0.9f}'.format(b)
            b = float(balance)
        c = exchange.fetch_ticker('ETH/USDT')
        c = c['bid']
        if is_exponential(c) == True:
            balance = '{:0.9f}'.format(c)
            c = float(balance)
        d = exchange.fetch_ticker('OKB/USDT')
        d = d['bid']
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/OKB'
            pair2 = 'XRP/ETH'
        print(f"Изменение в цене: {end}")
    pair10()
    def pair11():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/OKB')
        a = a['bid']
        print(a)
        b = exchange.fetch_ticker('XRP/BTC')
        b = b['bid']
        if is_exponential(b) == True:
            balance = '{:0.9f}'.format(b)
            print(balance)
            b = balance
            print(b)
        print(b)
        c = exchange.fetch_ticker('BTC/USDT')
        c = c['bid']
        if is_exponential(c) == True:
            balance = '{:0.9f}'.format(c)
            c = balance
        print(c)
        d = exchange.fetch_ticker('OKB/USDT')
        d = d['bid']
        print(d)
        step1 = get_balance/c
        step2 = step1/a
        step3 = step2*b
        step4 = step3*d
        end = step4-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/OKB'
            pair2 = 'XRP/BTC'
        print(f"Изменение в цене: {end}")
    # pair11()
    def pair12():
        global max_price, pair1, pair2
        get_balance = get_USDT()
        a = exchange.fetch_ticker('XRP/OKB')
        a = a['bid']
        b = exchange.fetch_ticker('XRP/USDT')
        b = b['bid']
        d = exchange.fetch_ticker('OKB/USDT')
        d = d['bid']
        step1 = get_balance/d
        step2 = step1/a
        step3 = step2*b
        end = step3-get_balance
        if max_price < end:
            max_price = end
            pair1 = 'XRP/OKB'
            pair2 = 'XRP/USDT'
        print(f"Изменение в цене: {end}")
    pair12()
    print(f"Максимальное изменение: {max_price} Пара 1: {pair1} Пара 2:{pair2}")
    if max_price >= 0.02:
        open_order(pair1, pair2)


def open_order(pair1, pair2):
    print("Функция вызвана")
    while True:
        print("Цикл запущен")
        balance_USDT = get_USDT()
        pair_list1 = pair1.split('/')
        pair_list2 = pair2.split('/')
        if pair_list1[0] and pair_list1[1] and pair_list2[0] and pair_list2[1] != 'USDT':
            element = pair_list1[1] # Монета, которую нужно купить за USDT
            pair_element_B = element+'/USDT' # Формирование пары для покупки монеты
            print("Вывод пары в 1 цикле:", pair_element_B)
            price_USDT_pair = exchange.fetch_ticker(pair_element_B)
            price_USDT_pair = price_USDT_pair['bid'] # Получение уены пары для работы с монетой Цена 1 пары

            element2 = pair_list2[1] # Монета, которую нужно продать для USDT
            pair_element2_U = element2+'/USDT' # Формирование пары для продажи монеты
            price_pair_USDT = exchange.fetch_ticker(pair_element2_U) # Цена 4 пары
            price_pair_USDT = price_pair_USDT['ask']

            pair_2 = exchange.fetch_ticker(pair1) # Цена 2 пары
            pair_2 = pair_2['bid']

            pair_3 = exchange.fetch_ticker(pair2) # Цена 3 пары
            pair_3 = pair_3['ask']

            sum = balance_USDT/price_USDT_pair
            sum1 = sum/pair_2
            sum2 = sum1*pair_3
            sum3 = sum2*price_pair_USDT

            end = sum3-balance_USDT
            print(end)
            if end >= 0.04:
                try:
                    balance = balance_USDT/float(price_USDT_pair)
                    order = exchange.create_order(symbol=pair_element_B, type='market', side='buy',  amount=balance_USDT)
                    print('Ордер успешно размещен')
                    print(balance_USDT)
                except ccxt.BaseError as e:
                    print('Произошла ошибка при размещении ордера:', str(e))

                balance = get_balance(pair_list1[1])/pair_2
                print(balance)
                try:
                    order = exchange.create_order(symbol=pair1, type='market', side='buy',  amount=balance)
                    print('Ордер успешно размещен')

                except ccxt.BaseError as e:
                    print('Произошла ошибка при размещении ордера:', str(e))

                promej_balance = pair_list2[0]
                balance = float(get_balance(promej_balance))
                print(balance)
                try:
                    order = exchange.create_order(symbol=pair2, type='market', side='sell',  amount=balance)
                    print('Ордер успешно размещен:')


                except ccxt.BaseError as e:
                    print('Произошла ошибка при размещении ордера:', str(e))

                promej_balance = float(get_balance(pair_list2[1]))
                print(promej_balance)
                try:
                    order = exchange.create_order(symbol=pair_element2_U, type='market',  side='sell',  amount=promej_balance)
                    print('Ордер успешно размещен:')

                except ccxt.BaseError as e:
                    print('Произошла ошибка при размещении ордера:', str(e))
            else:
                  break
        print("До проверки")
        if pair2 == 'XRP/USDT':
            print("Проверка запущена")
            pair_1_USDT = exchange.fetch_ticker(pair1)
            pair_1_U = pair_1_USDT['bid'] # Цена 2 пары 
            print("Цена 2 получена")
            pair_2_U = exchange.fetch_ticker(pair2)
            pair_2_U = pair_2_U['ask'] # Цена 3 пары

            pair_3_UU= pair_list1[1]
            pair_3_UU = pair_3_UU+'/USDT'
            print("Вывод пары во втором цикле:", pair_3_UU)
            pair_3_USDT = exchange.fetch_ticker(pair_3_UU) # цена 1 пары
            pair_3_U = pair_3_USDT['bid'] 

            sum = balance_USDT/pair_3_U
            sum1 = sum/pair_1_U
            sum2 = sum1*pair_2_U

            end = sum2-balance_USDT
            print("2 проверка:", end)
            if end >= 0.04:
                try:
                    balance = balance_USDT/pair_3_U
                    print("Баланс USDT", balance)
                    order = exchange.create_order(symbol=pair_3_UU, type='market',  side='buy',  amount=balance)
                    balance = get_balance(pair_list1[1])/pair_1_U
                    print("Количество XRP", balance)
                    order = exchange.create_order(symbol=pair1, type='market',  side='buy',  amount=balance)
                    balance = get_balance(pair_list2[0])
                    print("Количество монеты длля продажи", balance)
                    order = exchange.create_order(symbol=pair2, type='market',  side='sell',  amount=balance)
                except ccxt.BaseError as e:
                    print("Ошибка", str(e))
            else:
                break 
while True:
    pairs()

