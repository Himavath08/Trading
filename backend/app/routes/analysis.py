from fastapi import APIRouter

from app.services.market_service import MarketService
from app.services.gemini_service import GeminiService

from app.agents.quant_agent import QuantAgent
from app.agents.sentiment_agent import SentimentAgent
from app.agents.news_agent import NewsAgent
from app.agents.risk_agent import RiskAgent
from app.agents.portfolio_manager import PortfolioManager

router = APIRouter()

market_service = MarketService()

gemini_service = GeminiService()

quant_agent = QuantAgent()
sentiment_agent = SentimentAgent()
news_agent = NewsAgent()
risk_agent = RiskAgent()
portfolio_manager = PortfolioManager()

@router.get("/analyze/{ticker}")

async def analyze_stock(
    ticker: str
):

    df = market_service.get_stock_data(
        ticker
    )

    quant = quant_agent.analyze(df)

    news = news_agent.fetch_news(
        ticker
    )

    sentiment = sentiment_agent.analyze(
        news
    )

    risk = risk_agent.evaluate(
        quant
    )

    decision = portfolio_manager.decide(
        sentiment,
        risk
    )

    memo = gemini_service.generate_memo(
        ticker,
        quant,
        sentiment,
        risk,
        decision
    )

    return {
        "ticker": ticker,
        "quant": quant,
        "news": news,
        "sentiment": sentiment,
        "risk": risk,
        "decision": decision,
        "memo": memo
    }