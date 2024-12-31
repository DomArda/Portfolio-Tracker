import configparser
import json
import csv
import os
import traceback

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
    """Factory interface for handling configuration files."""

    @staticmethod
    def _init():
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
            Config._init()

            if os.path.exists(self._ini_file_dir):
                # .ini file exists
                try:
                    self.read()

                except:
                    # Failure
                    os.remove(self._ini_file_dir)
                    open(self._ini_file_dir, "x")

            else:
                # no .ini file
                open(self._ini_file_dir, "x")

        def read(self):
            """Reads .ini file into memory."""
            self.ConfigParser.read(self._ini_file_dir)

        def write(self):
            """Writes from memory to local storage."""
            with open(self._ini_file_dir, "w") as ini:
                self.ConfigParser.write(ini)

        def get(self, platform : str, key_name : str = "API_key") -> str:
            """
            Retrieve the specified key for the platform if it exists.

            Args:
                platform (str): The platform to search for.
                key_name (str): The specific key to retrieve, default is "API_key".

            Returns:
                str: The saved key or an empty string if no key exists.
            """
            return self.ConfigParser.get(platform, key_name)

        def set(self, platform, value : str, key_name : str = "API_key"):
            """
            Set the key for the platform, creating a new section if the platform doesn't exist, overwriting otherwise.

            **NOTE:** This will only save the key and platform to the configuration saved in memory, call the write()
            method to flush to disk.

            Args:
                platform (str): The platform to save the associated key to.
                key_name (str): The key name, default is "API_key".
                value(str): The value of the key.

            """
            if self.has(platform):
                self.ConfigParser.set(platform, key_name, value)
            self.ConfigParser[platform] = {key_name: value}

        def remove(self, platform):
            """
            Remove a platform from the .ini file, this will remove all associated keys.

            Args:
                platform (str): The platform to remove from the .ini file.
            """
            self.ConfigParser.remove(platform)

        def remove_key(self, platform, key_name):
            """
            Remove a key from a platform in the .ini file.

            Args:
                platform (str): The platform to search for.
                key_name (str): The key name to remove.
            """
            self.ConfigParser.remove_option(platform, key_name)

        def has(self, platform : str) -> bool:
            """
            Check whether a section exists for the specified platform.

            Args:
                platform (str): The platform to check for.

            Returns:
                bool: True if the section exists, False otherwise.
            """
            return self.ConfigParser.has_section(platform)


    class Json:
        """Abstract interface for handling .json files."""

        def __init__(self):
            Config._init()

    class Csv:
        """Abstract interface for handling .csv files."""

        def __init__(self):
            Config._init()