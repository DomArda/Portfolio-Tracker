import configparser
import json
import csv
import os

_cur_dir = os.path.dirname(os.path.abspath(__file__))
_local_dir = os.path.join(_cur_dir, "local")

# Currently, there is no known idea on how to approach CSV files.
# As CSV files will only be useful for storing account's histories
# And is what is considered the industry standard anyway.
# Possibilities include:
# 1. Have a separate file for all trading platform's history
# 2. Use pandas to combine all CSV data into one single CSV file (like for JSON)

# This also raises the question for compatibility with 'manual' CSV data
# such as the user providing a CSV file because we don't support a broker.
_csv_dir = os.path.join(_cur_dir, "csv-storage")

class Config:
    """Abstract interface for handling configuration files."""

    @staticmethod
    def init():
        """
        Creates the folder structure.

        Doesn't care if the folder already exists.
        """
        os.makedirs(_local_dir, exist_ok=True)


    class Ini:
        """Abstract interface for handling .ini files."""
        _ini_file_dir = os.path.join(_local_dir, "keys.ini")
        ConfigParser = configparser.ConfigParser()

        def __init__(self):
            Config.init()

            if os.path.exists(self._ini_file_dir):
                # .ini file exists
                self.ConfigParser.read(self._ini_file_dir)

            else:
                # no .ini file
                open(self._ini_file_dir, "x")

    class Json:
        """Abstract interface for handling .json files."""

    class Csv:
        """Abstract interface for handling .csv files."""