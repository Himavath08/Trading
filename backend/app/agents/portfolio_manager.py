class PortfolioManager:

    def decide(
        self,
        sentiment,
        risk
    ):

        if (
            sentiment["label"] == "POSITIVE"
            and risk == "LOW RISK"
        ):
            return "PROCEED"

        return "ABORT"