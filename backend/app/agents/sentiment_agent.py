class SentimentAgent:

    def analyze(self, news):

        positive_words = [
            "growth",
            "profit",
            "bullish",
            "surge"
        ]

        score = 0

        for headline in news:

            for word in positive_words:

                if word in headline.lower():
                    score += 1

        if score >= 2:
            return {
                "label": "POSITIVE",
                "score": 0.87
            }

        return {
            "label": "NEGATIVE",
            "score": 0.41
        }