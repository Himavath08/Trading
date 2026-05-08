import yfinance as yf

class MarketService:

    def get_stock_data(self, ticker: str):

        df = yf.download(
            ticker,
            period="6mo",
            interval="1d"
        )

        return df