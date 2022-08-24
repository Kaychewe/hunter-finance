"""
    file: test-gui.py
    author: Kasonde Chew
    
    Program is basic GUI interface test for the Hunter Forex Finance Application
    
    Modules (experimental)
    1. Fundamental Data 
        bls-data 
        
    2. Technical Data
        yfinance & pandas-datareader
        
    3. Data Visulaization Basics 
        matplotlib
        pandas
        numpy
        
        
        
        
"""

# YFinance Module Testing 

import pandas as pd
import yfinance as yf 

df_yahoo = yf.download('AAPL', start='2022-01-01', end='2022-08-23',progress=False)

print(df_yahoo)