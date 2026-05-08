import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

class GeminiService:

    def generate_memo(
        self,
        ticker,
        quant,
        sentiment,
        risk,
        decision
    ):

        prompt = f"""
        Generate a professional AI investment memo.

        Ticker: {ticker}

        Quantitative Analysis:
        {quant}

        Sentiment:
        {sentiment}

        Risk:
        {risk}

        Final Decision:
        {decision}

        Include:
        - Technical outlook
        - Risk assessment
        - Opportunities
        - Final recommendation
        """

        response = model.generate_content(
            prompt
        )

        return response.text