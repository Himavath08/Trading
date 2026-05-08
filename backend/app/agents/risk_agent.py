class RiskAgent:

    def evaluate(self, quant):

        if quant["volatility"] > 0.04:
            return "HIGH RISK"

        if quant["rsi"] > 70:
            return "OVERBOUGHT"

        return "LOW RISK"