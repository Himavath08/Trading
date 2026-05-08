from pydantic import BaseModel

class AnalysisResponse(BaseModel):

    ticker: str
    quant: dict
    sentiment: dict
    risk: str
    decision: str
    memo: str