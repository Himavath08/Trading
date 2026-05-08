from ta.momentum import RSIIndicator
from ta.trend import MACD

class QuantAgent:

    def analyze(self, df):

        close = df["Close"]

        rsi = RSIIndicator(
            close
        ).rsi().iloc[-1]

        macd = MACD(
            close
        ).macd_diff().iloc[-1]

        volatility = (
            close.pct_change().std()
        )

        return {
            "rsi": round(float(rsi), 2),
            "macd": round(float(macd), 2),
            "volatility": round(
                float(volatility),
                4
            )
        }