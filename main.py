from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
import requests

#TODO
# prompt the user to write requested crypto and amount holding      - ✓
# calculate the value of the user'c coin in $ and €                 - ✓
# list all crypto and prices as first option for user               - 

# initialize colorama
init()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_02) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}
url = 'https://finance.yahoo.com/crypto'
url_two = 'https://finance.yahoo.com/quote/EURUSD%3DX?p=EURUSD%3DX'


response = requests.get(url, headers=headers)
response_two = requests.get(url_two, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
soup_eur= BeautifulSoup(response_two.content, 'lxml')
eur = soup_eur.select('[data-test=qsp-price]')[0].get_text()
float(eur)

print('')
print('***************************Crypto Prices***************************')
print('')
print(f'Current value of an euro is:{Fore.LIGHTYELLOW_EX} {eur}${Fore.RESET}')
print('')
selected_coin = input("Choose crypto - (BTC, ETH, etc.) or insert 'A' to list each one: ")

# amount = input('Input your amount of Ethereum: ')

for i in soup.select('.simpTblRow'):
    crypto_symbol = i.select('[aria-label=Symbol]')[0].get_text()
    crypto_price = i.select('[aria-label*=Price]')[0].get_text().replace(',', '')
    if selected_coin.upper() == crypto_symbol[:-4]:
        print('Input the amount of specified coin, if the value equals 0, the current price will be shown instead.')
        print('*******************************************************************')
        print('')
        amount = input('The amount: ')
        print('')
        print('*******************************************************************')
        if float(amount) != 0.00:
            calc_price_usd = float(crypto_price)*float(amount)
            calc_price_eur = (float(crypto_price)*float(amount))/float(eur)
            print(Back.LIGHTRED_EX ,f'Crypto: {Fore.LIGHTYELLOW_EX} {crypto_symbol[:-4]} {Fore.RESET}', Back.RESET)
            print('')
            print(Back.GREEN, f'Value in $: {Fore.LIGHTYELLOW_EX} {calc_price_usd:.2f} {Fore.RESET}', Back.RESET)
            print('')
            print(Back.GREEN, f'Value in €: {Fore.LIGHTYELLOW_EX} {calc_price_eur:.2f} {Fore.RESET}', Back.RESET)
            print('----------------------------')
        else:
            print(Back.LIGHTRED_EX,'Crypto:', Fore.LIGHTYELLOW_EX, crypto_symbol, Fore.RESET, Back.RESET)
            print('')
            print(Back.GREEN,'Price:', Fore.LIGHTYELLOW_EX,crypto_price, Fore.RESET, Back.RESET)
            print('----------------------------')
    elif selected_coin.upper() == "A":
        print('')
        print('Cryptocurrency:', Back.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, crypto_symbol[:-4], Fore.RESET, Back.RESET)
        print('')
        print('Price:           ',Back.GREEN, Fore.LIGHTYELLOW_EX, crypto_price, '$', Fore.RESET, Back.RESET)
        print('----------------------------')
