import requests
from datetime import datetime

class APIService:
    """General interface for API usage."""
    BASE_URL = None
    API_key = None

    def __init__(self, API_key):
        self.API_key = API_key

    def request(self,
                endpoint : str,
                params : dict = None,
                method: str = "GET",
                ) -> dict:
        """
        Sends a request to the specified API endpoint.

        Args:
            endpoint (str): The API endpoint to send the request to.
            params (dict): Additional parameters for the request.
            method (str): The HTTP method of the request, defaults to GET.

        Returns:
           dict: The response from the specified API endpoint.

        Raise:
            ValueError: Illegal method specified or method not implemented.
            HTTPError: If any HTTP error has occurred.
        """

        url = self.BASE_URL + endpoint

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.API_key
        }

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=params)

            elif method == "POST":
                response = requests.post(url, headers=headers, json=params)

            elif method == "PUT":
                response = requests.put(url, headers=headers, json=params)

            elif method == "DELETE":
                response = requests.delete(url, headers=headers, json=params)

            else:
                raise ValueError(f"'{method}' is not a valid method.")

        except requests.exceptions.HTTPError as err:
            raise err

        return response.json()

class Trading212(APIService):
    """
    API class for Trading212

    Main: https://app.trading212.com\n
    API Docs: https://t212public-api-docs.redoc.ly
    """
    BASE_URL = "https://live.trading212.com"

    # Instruments Metadata

    # Pies

    # Equity Orders

    # Account Data
    def fetch_account_cash(self) -> dict:
        """Return a dict of monetary information about the account."""
        return super().request("/api/v0/equity/account/cash")

    def fetch_account_metadata(self) -> dict:
        """Return a dict of information about the account."""
        return super().request("/api/v0/equity/account/info")

    # Personal Portfolio
    def fetch_all_open_positions(self) -> dict:
        """Return a dict of all currently open positions."""
        return super().request("/api/v0/equity/portfolio")

    def search_for_a_specific_position_by_ticker(self, ticker : str) -> dict:
        """Search for an open position by ticker."""
        return super().request("/api/v0/equity/portfolio/ticker", {"ticker": ticker}, "POST")

    def fetch_a_specific_position(self, ticker : str) -> dict:
        """Fetch an open position by ticker."""
        return super().request("/api/v0/equity/portfolio/")

    # Historical Items
    def historical_order_data(self,
                              cursor : int = 0,
                              ticker : str = None,
                              limit : int = 50
                              ) -> dict:
        """
        Return a dict of historical order information.

        Args:
            cursor (int): The pagination cursor of the historical order.
            ticker (str): The ticker symbol to filter for.
            limit (int): The maximum number of historical orders to return.
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().request("/api/v0/equity/history/orders", query)

    def paid_out_dividends(self,
                            cursor : int = 0,
                            ticker : str = None,
                            limit : int = 50
                            ) -> dict:
        """
        Return a dict of all historical dividend payments.

        Args:
            cursor (int): The pagination cursor of the historical order.
            ticker (str): The ticker symbol to filter for.
            limit (int): The maximum number of historical orders to return.
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().request("/api/v0/history/dividends", query)

    def exports_list(self) -> dict:
        """Return a dict of all CSV export data."""
        return super().request("/api/v0/history/exports")

    def export_csv(self,
                   include_dividends : bool = True,
                   include_interest : bool = True,
                   include_orders : bool = True,
                   include_transactions : bool = True,
                   time_from : datetime = datetime(1970, 1, 1).isoformat(),
                   time_to : datetime = datetime.now().isoformat(),
                   ) -> dict:
        """
        Send a POST request to create a CSV export file for the account.

        Args:
            include_dividends (bool): Include dividends in the export file.
            include_interest (bool): Include interest in the export file.
            include_orders (bool): Include orders in the export file.
            include_transactions (bool): Include transactions in the export file.
            time_from (datetime): When the data should start being recorded, should be in ISO 8601 format.
            time_to (datetime): When the data should end being recorded, should be in ISO 8601 format.
        """
        payload = {
            "dataIncluded": {
                "includeDividends": include_dividends,
                "includeInterest": include_interest,
                "includeOrders": include_orders,
                "includeTransactions": include_transactions
            },
            "timeFrom": time_from,
            "timeTo": time_to
        }
        return super().request("/api/v0/history/exports", payload, "POST")

    def transaction_list(self,
                         cursor : int = 0,
                         time : datetime = datetime(1970, 1, 1).isoformat(),
                         limit : int = 50
                         ) -> dict:
        """
        Return information about monetary movements in and out of the account.

        Args:
            cursor (int): The pagination cursor of the transaction page.
            time (datetime): Retrieve transactions after this time, should be in ISO 8601 format.
            limit (int): The maximum number of transactions to return.
        """
        return super().request("/api/v0/history/transactions")



