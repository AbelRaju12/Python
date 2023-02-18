import pandas as pd
import yfinance as yf
import urllib.request,json,requests,matplotlib
amd = yf.Ticker("AAPL")
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(amd_info)
print(amd_info['country'])
print(amd_info['sector'])
#print(amd_info['longBusinessSummary'])
amd_share=amd.history(period="max")
amd_share.reset_index(inplace=True)
print(amd_share.plot(x="Date", y="Open"))

