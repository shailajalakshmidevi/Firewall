# -*- coding: utf-8 -*-

import sys
import os
import unittest

# Add src and tests directories to sys.path to allow importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

# Assuming 'main' function is in the core.py module
from core import main

if __name__ == '__main__':
    # Debugging: Print the current working directory to verify where the script is running
    print("Current working directory:", os.getcwd())
    
    # Define the file path relative to the firewall directory (moving up one level from src)
    file_path = '../packets/tcp.txt'  # Use relative path, moving up from 'src' to 'firewall'
    
    # Check if the file exists
    if os.path.exists(file_path):
        try:
            # Open the file and pass it to the main function
            with open(file_path, 'r') as f:
                print(f"Reading from file: {file_path}")
                main(f)  # Pass the file object to the main function
        except Exception as e:
            print(f"Error while processing file {file_path}: {e}")
    else:
        print(f"Error: The file '{file_path}' does not exist.")
