import yfinance as yf

# Obtener datos de AAPL
aapl = yf.Ticker("AAPL")
data = aapl.history(period="1d")

print(f"Último precio de cierre de AAPL: {data['Close'].iloc[-1]}")
