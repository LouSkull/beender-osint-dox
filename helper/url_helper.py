import sys
import os
import json
from helper import printer


def read_local_content(path):
    try:
        with open(resource_path(path), 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        printer.error(f"An error occurred: {str(e)}")
        return None


def read_local_json_content(path):
    try:
        with open(resource_path(path), 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        printer.error(f"An error occurred: {str(e)}")
        return None

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
