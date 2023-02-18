import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json,urllib.request,requests
from bs4 import BeautifulSoup

tesla = yf.Ticker('TSLA')
tesla_info=tesla.history(period="max")
#print(tesla_info)
tesla_info.reset_index(inplace=True)
print(tesla_info.head())

rev_url_tesla="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_rev_tesla=requests.get(rev_url_tesla).text
soup=BeautifulSoup(html_rev_tesla,"html.parser")
#print(soup.find_all('body'))
tesla_rev = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    rev = col[1].text.replace("$", "").replace(",", "")
    tesla_rev = tesla_rev.append({"Date": date, "Revenue": rev}, ignore_index = True)
tesla_rev.dropna(inplace=True)
tesla_rev = tesla_rev[tesla_rev['Revenue'] != ""]
print(tesla_rev.head(20))

Gamestop=yf.Ticker("GME")
gms_info=Gamestop.history(period="max")
#print(gms_info)
gms_info.reset_index(inplace=True)
print(gms_info.head())   

rev_url_gms="https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_rev_gms=requests.get(rev_url_gms).text
soup=BeautifulSoup(html_rev_gms,"html.parser")
#print(soup.find_all('title'))
gms_rev = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    rev = col[1].text.replace("$", "").replace(",", "")
    gms_rev = gms_rev.append({"Date": date, "Revenue": rev}, ignore_index = True)
gms_rev.dropna(inplace=True)
gms_rev = gms_rev[gms_rev['Revenue'] != ""]
print(gms_rev.head(20))

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph(tesla_info,tesla_rev,"Tesla")

make_graph(gms_info,gms_rev,'Gamestop')