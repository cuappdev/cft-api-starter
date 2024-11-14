import json
import requests

class Coin:
    def __init__(self, id):
        self.id = id
        self.base_url = 'https://api.coingecko.com/api/v3'

    def get_price_usd(self):
        # TODO: Implement this method to get the price of the coin in USD
        """
        Step 1: Make a GET request to the CoinGecko API to get the price of the coin in USD 
        (Hint: use the /simple/price endpoint and pay attention to the parameters)
        Step 2: Parse the JSON response to get the price of the coin (Hint: use the `json` module)
        Step 3: Return the price of the coin (Hint: JSON data is a Python dictionary)
        """
        url = f'{self.base_url}/ENDPOINT'
        response = requests.get(url, params={})
        data = json.loads(response.text)
        return data
    
    def get_market_cap(self):
        # TODO: Implement this method to get the market cap of the coin
        pass
    
    def get_price_change_percentage_24h(self):
        # TODO: Implement this method to get the price change percentage in the last 24 hours
        pass
    
    def get_description(self):
        # TODO: Implement this method to get the description of the coin in English
        pass

