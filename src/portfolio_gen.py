class Portfolio:
    """General interface for a portfolio."""

    @staticmethod
    def filter_attributes(cls: object) -> dict:
        """Returns a dictionary of all attributes of a class or an instance that do not begin with '_', effectively
        returning all non-private attributes."""
        return {key: value for key, value in cls.__dict__.items() if not key.startswith("_")}

    @staticmethod
    def write(data : dict, cls : object):
        """
        Writes the dictionary data to the object's attributes.

        Args:
            data (dict): Dictionary data to write.
            cls (object): Object to write to.
        """
        for key, value in data.items():
            if hasattr(cls, key):
                if value is None: value = 0

                setattr(cls, key, value)

    @staticmethod
    def percentage_change(initial_value : float, final_value : float) -> float:
        """
        Return the percentage change between initial_value and final_value.

        Args:
            initial_value (float): Initial value.
            final_value (float): Final value.

        Return:
            float: Percentage change, zero if attempting to divide by zero.
        """

        if initial_value == 0: return 0

        return (final_value - initial_value) / initial_value * 100

    class Cash:
        """
        Interface for cash figures of a portfolio.

        Attributes:
            - free (float): Free cash.
            - blocked (float): Unavailable cash.
            - invested (float): Cash currently invested before fluctuation.
            - profit_and_loss (float): Unrealized net cash after investments.
            - result (float): Realized net cash after investments.
            - total (float): Total cash counts.
            - dividend_total (float): Total of dividend payment.
            - currency_code (str): Account's currency code.
        """
        free = 0
        blocked = 0
        invested = 0
        profit_and_loss = 0
        result = 0
        total = 0
        dividend_total = 0
        currency_code = "$"

    class Stock:
        """Interface for stock ownership of a portfolio."""