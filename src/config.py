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

_ini_file_dir = os.path.join(_local_dir, "keys.ini")
_json_file_dir = os.path.join(_local_dir, "portfolio.json")

_ini_parser = configparser.ConfigParser()

class Config:
    """Abstract interface for handling configuration files."""

    class Ini:
        """Abstract interface for handling .ini files."""

    class Json:
        """Abstract interface for handling .json files."""

    class Csv:
        """Abstract interface for handling .csv files."""