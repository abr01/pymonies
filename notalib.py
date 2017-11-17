Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> # Load the necessary packages and modules
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import fix_yahoo_finance
import pandas as pd

# Force Index 
def ForceIndex(data, ndays): 
 FI = pd.Series(data['Close'].diff(ndays) * data['Volume'], name = 'ForceIndex') 
 data = data.join(FI) 
 return data


# Retrieve the Apple Inc. data from Yahoo finance:
data = pdr.get_data_yahoo("AAPL", start="2010-01-01", end="2016-01-01") 
data = pd.DataFrame(data)

# Compute the Force Index for AAPL
n = 1
AAPL_ForceIndex = ForceIndex(data,n)
print(AAPL_ForceIndex)
