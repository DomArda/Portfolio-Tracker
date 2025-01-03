import api_interface
import portfolio_gen
from config import Config

_ini = Config.Ini()

API_key = input("Enter API Key:\n")

_ini.set("Trading212", API_key)
_ini.write()

Trading212_Portfolio = portfolio_gen.Portfolio()
Trading212_API = api_interface.Trading212(API_key)

portfolio_gen.Portfolio.write(Trading212_API.get_cash(), Trading212_Portfolio.Cash)

print(portfolio_gen.Portfolio.filter_attributes(Trading212_Portfolio.Cash))