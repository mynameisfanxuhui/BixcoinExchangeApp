import requests
import requests_cache
import model

requests_cache.install_cache('price_cache', backend='sqlite', expire_after=60)

def get_rates():
    results = []
    try:
        # bid stands for highest buy order as buy price. ask stands for lowest sell order as sell price
        bitstampBitcoin = requests.get(
            'https://www.bitstamp.net/api/v2/ticker/btcusd/').json()
        #print("Used Cache:", bitstamp.from_cache)
        oBitstampBitcoin = model.CCoin("bitstamp", "bitcoin", float(bitstampBitcoin["bid"]), float(bitstampBitcoin["ask"]))
        results.append(oBitstampBitcoin)
        bitstampEth = requests.get(
            'https://www.bitstamp.net/api/v2/ticker/ethusd/').json()
        oBitstampEth = model.CCoin("bitstamp", "eth", float(bitstampEth["bid"]), float(bitstampEth["ask"]))
        results.append(oBitstampEth)
        bittrexBitcoin = requests.get(
            'https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc').json()['result']
        oBittrexBitcoin = model.CCoin("bittrex", "bitcoin", float(bittrexBitcoin["Bid"]), float(bittrexBitcoin["Ask"]))
        results.append(oBittrexBitcoin)
        bittrexEth = requests.get(
            'https://bittrex.com/api/v1.1/public/getticker?market=usdt-eth').json()['result']
        oBittrexEth = model.CCoin("bittrex", "eth", float(bittrexEth["Bid"]), float(bittrexEth["Ask"]))
        results.append(oBittrexEth)

        return results
    except:
        return False


# test get data
if __name__ == '__main__':
    data = get_rates()
    print(data)