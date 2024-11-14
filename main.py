from coin import Coin

def main():
    btc = Coin('bitcoin')
    print(f'Price of Bitcoin in USD: {btc.get_price_usd()}')
    print(f'Market cap of Bitcoin: {btc.get_market_cap()}')

    eth = Coin('ethereum')
    print(f'Price of Ethereum in USD: {eth.get_price_usd()}')
    print(f'Market cap of Ethereum: {eth.get_market_cap()}')

    doge = Coin('dogecoin')
    print(f'Price of Dogecoin in USD: {doge.get_price_usd()}')
    print(f'Market cap of Dogecoin: {doge.get_market_cap()}')

    # TODO: Find the coin with the highest market cap

    # TODO: Find the most volatile coin
    # Eg. The coin with the highest absolute price change percentage in the last 24 hours

    # TODO: Take user input and print the price of the coin in USD, the market cap, and the description of the coin in English
    # input_id = input('Enter the id of a coin: ')

if __name__ == '__main__':
    main()