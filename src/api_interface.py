import api_service
from currency_symbols import CurrencySymbols

class APIInterface:
    """Inheritable abstract base class APIInterface."""

    def get_cash(self) -> dict:
        """Return a dict that fills the Cash attribute of a Portfolio instance."""

class Trading212(APIInterface):
    """API Interface for Trading212"""

    def __init__(self, API_key):
        self.Platform = api_service.Trading212(API_key)

    def get_cash(self):
        cash_dict = {}

        fetch_account_cash = self.Platform.fetch_account_cash()
        """
        {
            "blocked": 0,
            "free": 0,
            "invested": 0,
            "pieCash": 0,
            "ppl": 0,
            "result": 0,
            "total": 0
        }
        """
        cash_dict['free'] = fetch_account_cash['free']
        cash_dict['blocked'] = fetch_account_cash['blocked']
        cash_dict['invested'] = fetch_account_cash['invested']
        cash_dict['profit_and_loss'] = fetch_account_cash['ppl']
        cash_dict['result'] = fetch_account_cash['result']
        cash_dict['total'] = fetch_account_cash['total']

        fetch_account_metadata = self.Platform.fetch_account_metadata()
        """
        {
            "currencyCode": "USD",
            "id": 0
        }
        """
        cash_dict['currency_code'] = CurrencySymbols.get_symbol(fetch_account_metadata['currencyCode'])

        paid_out_dividends = self.Platform.paid_out_dividends()
        """
        {
            "items": [
                {
                    "amount": 0,
                    "amountInEuro": 0,
                    "grossAmountPerShare": 0,
                    "paidOn": "2019-08-24T14:15:22Z",
                    "quantity": 0,
                    "reference": "string",
                    "ticker": "string",
                    "type": "string"
                }
            ],
            "nextPagePath": "string"
        }
        """
        dividend_total = 0

        for payment in paid_out_dividends['items']:
            dividend_total += payment['amount']

        cash_dict['dividend_total'] = dividend_total

        return cash_dict
