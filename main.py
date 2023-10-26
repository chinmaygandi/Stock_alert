import requests
from datetime import datetime, timedelta
import streamlit as st
st.title("Stock Selection App")

# Create a list of stock symbols
stocks = ["AAPL","MSFT","AMZN","NVDA","GOOGL","GOOG","META","BRK.B","TSLA","UNH","LLY","XOM","JPM","V","JNJ","AVGO","PG","MA","CVX","HD","MRK","ABBV","ADBE","COST","WMT","PEP","CSCO","KO","CRM","MCD","ACN","BAC","TMO","LIN","NFLX","CMCSA","PFE","ABT","AMD","ORCL","DIS","AMGN","COP","WFC","INTC","PM","INTU","DHR","TXN","VZ","UNP","CAT","NKE","IBM","QCOM","HON","BMY","GE","SPGI","AMAT","LOW","NOW","UPS","T","SBUX","ELV","RTX","NEE","TJX","DE","BA","ADP","LMT","GS","BKNG","GILD","MDT","PLD","ISRG","MS","VRTX","MMC","CI","PGR","SYK","CVS","MDLZ","REGN","BLK","CB","ADI","SLB","AXP","LRCX","EOG","ETN","ZTS","CME","C","MO","SCHW","BDX","AMT","PANW","MU","BSX","SO","SNPS","TMUS","NOC","FI","DUK","BX","EQIX","CDNS","HUM","AON","KLAC","APD","ICE","CSX","ITW","MCK","CL","MPC","PYPL","PXD","WM","SHW","FDX","ORLY","GD","EMR","ROP","PSX","CMG","TGT","ABNB","AJG","MCO","HCA","FCX","USB","PH","NXPI","MMM","APH","MAR","MSI","ANET","VLO","F","NSC","LULU","TDG","AZO","HES","PNC","CHTR","WELL","ADSK","OXY","SRE","CTAS","TT","PCAR","WMB","AIG","EW","AFL","KMB","MCHP","GM","ECL","CARR","PSA","ROST","OKE","EXC","ADM","CNC","MSCI","HLT","MET","CPRT","HAL","AEP","CCI","PAYX","BIIB","MNST","STZ","GIS","TRV","TEL","ON","FTNT","TFC","CEG","CTVA","IDXX","ODFL","NUE","DLR","O","BKR","SPG","DOW","COF","VRSK","KVUE","IQV","YUM","DD","PCG","D","LHX","DXCM","CTSH","JCI","SYY","FAST","KMI","PRU","AME","BK","A","ALL","AMP","OTIS","EL","XEL","COR","EA","CMI","DVN","NEM","GWW","DHI","ACGL","ROK","CSGP","ED","FIS","FANG","RSG","PEG","PPG","GPN","KDP","KR","HSY","URI","VICI","IT","CDW","WST","VMC","MRNA","LEN","APTV","WEC","DG","MLM","GEHC","KHC","FTV","IR","ANSS","EIX","PWR","AVB","CAH","LYB","EXR","DLTR","WBD","FICO","HPQ","AWK","MTD","TTWO","CHD","CTRA","XYL","KEYS","ZBH","EBAY","TROW","EFX","WTW","HIG","STE","WY","TSCO","RMD","CBRE","SBAC","GLW","DAL","STT","DFS","BR","MOH","MPWR","DTE","ETR","AEE","HPE","EQR","TRGP","ALGN","MTB","DOV","RCL","ILMN","ES","VRSN","ULTA","TDY","FE","GPC","INVH","RJF","NVR","WAB","LH","FLT","PPL","MRO","IRM","CNP","NDAQ","CBOE","EG","EXPD","HWM","DRI","VTR","IFF","J","HOLX","BAX","FDS","PTC","ALB","ATO","FSLR","COO","CF","GRMN","AKAM","FITB","BRO","NTAP","CINF","CMS","EQT","STLD","TYL","VLTO","BG","PHM","WBA","CLX","PFG","TXT","WAT","MKC","HUBB","MAA","AXON","LVS","ARE","SWKS","OMC","IEX","JBHT","LUV","TER","AVY","BALL","HBAN","DGX","WDC","ESS","RF","SNA","ENPH","BBY","NTRS","TSN","K","APA","PKG","LKQ","STX","EXPE","WRB","CAG","EPAM","RVTY","LDOS","PAYC","POOL","LW","AMCR","LNT","DPZ","TRMB","SWK","SYF","MOS","L","IP","NDSN","SJM","UAL","CE","LYV","CFG","MAS","VTRS","EVRG","HST","CCL","TAP","IPG","CDAY","UDR","ZBRA","JKHY","INCY","KIM","PNR","NI","TECH","PODD","BF.B","MTCH","KMX","CHRW","CPT","MGM","REG","GEN","GL","CRL","NRG","AES","ROL","KEY","BWA","PEAK","HRL","HSIC","MKTX","TFX","QRVO","FFIV","CZR","WRK","HII","ALLE","EMN","WYNN","FMC","PNW","AOS","JNPR","NWSA","ETSY","RHI","CPB","FOXA","AIZ","UHS","CTLT","BXP","AAL","HAS","BBWI","WHR","XRAY","TPR","BIO","BEN","FRT","VFC","IVZ","NCLH","PARA","GNRC","CMA","RL","SEDG","ZION","SEE","DVA","MHK","ALK","FOX","NWS"]

# Checkbox to select all stocks
select_all_stocks = True  # Change to False to select specific stocks

# Allow the user to select individual stocks
selected_stocks = []
if select_all_stocks:
    selected_stocks = stocks
else:
    # Replace ["AAPL", "MSFT"] with the specific stocks you want to select
    selected_stocks = ["AAPL", "MSFT"]

all_stocks = []

for stock_symbol in selected_stocks:
    api_key = st.secrets["api_key"]
    price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"

    response = requests.get(price_url)
    if response.status_code != 200:
        print(f"Failed to fetch data for {stock_symbol}")
        continue

    data = response.json()
    #today = datetime(2023, 5, 11)  # Set the specific date to May 11, 2023
    today = datetime.now().date() - timedelta(days=1)

    time_series = data.get("Time Series (Daily)", {})

    # Convert today to the date format used in the JSON response
    today_str = today.strftime("%Y-%m-%d")

    if today_str in time_series:
        close_value = time_series[today_str]["4. close"]
    else:
        continue

    low_date = today
    low_value = close_value
    last_30_days = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]

    date_price_map = {}

    for date in last_30_days:
        if date in time_series:
            close_value = time_series[date]["4. close"]
            date_price_map[date] = float(close_value)

            if float(close_value) < float(low_value):
                low_date = date
                low_value = close_value

    if low_date == today:
        rsi_url = f"https://www.alphavantage.co/query?function=RSI&symbol={stock_symbol}&interval=daily&time_period=10&series_type=open&apikey={api_key}"
        response = requests.get(rsi_url)
        if response.status_code != 200:
            continue

        rsi_data = response.json()
        technical_analysis_rsi = rsi_data.get("Technical Analysis: RSI", {})

        if not technical_analysis_rsi:
            continue

        rsi_values = {date: float(data["RSI"]) for date, data in technical_analysis_rsi.items() if date in last_30_days}

        smallest_value = min(date_price_map.values())
        second_smallest_value = min(value for value in date_price_map.values() if value != smallest_value)
        smallest_key = [key for key, value in date_price_map.items() if value == smallest_value][0]
        second_smallest_key = [key for key, value in date_price_map.items() if value == second_smallest_value][0]

        if rsi_values.get(second_smallest_key, 0) < rsi_values.get(today_str, 0):
            all_stocks.append(stock_symbol)

if not all_stocks:
    st.success("No stocks observed")
else:
    st.success("The list of selected stocks are as below:")
    st.write(", ".join(all_stocks))
