import requests
import json

URL = 'http://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8'

payload = {}
headers= {
  "apikey": "KgVLymtQXiy9qzTQI6fqPmGqDXIyb0lo"
}

# FROM https://github.com/turtlecode/Make-Currency-Rate-App-Python-API/blob/main/currency.py FROM 
import requests
#URL = 'http://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8'


# FROM https://data-flair.training/blogs/currency-converter-python/
class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']
        
url = URL
converter = RealTimeCurrencyConverter(url)
items = converter.currencies
chosen_rates = []
print("items", items)
for name in items:
    print("currency name: ", name)
    rate = items[name]
    print("currency rate: ", rate)
    if rate < 10:
        chosen_rates.append(name)
print("CHOSEN RATES: ", chosen_rates)
    
