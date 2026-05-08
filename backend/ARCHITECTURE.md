# Trading Backend Architecture

## Project Structure

```
backend/
│
├── app/
│   │
│   ├── agents/                 # AI agents for analysis
│   │   ├── quant_agent.py      # Quantitative analysis agent
│   │   ├── sentiment_agent.py  # Sentiment analysis agent
│   │   ├── news_agent.py       # News analysis agent
│   │   ├── risk_agent.py       # Risk assessment agent
│   │   └── portfolio_manager.py # Portfolio management agent
│   │
│   ├── services/               # External service integrations
│   │   ├── market_service.py   # Market data service
│   │   ├── gemini_service.py   # Google Gemini AI integration
│   │   ├── websocket_manager.py # WebSocket connection manager
│   │   └── cache_service.py    # Caching layer
│   │
│   ├── websocket/              # WebSocket handling
│   │   └── socket.py           # WebSocket manager and handlers
│   │
│   ├── tasks/                  # Async background tasks
│   │   └── analysis_tasks.py   # Celery tasks for analysis
│   │
│   ├── routes/                 # API endpoints
│   │   ├── analysis.py         # Analysis endpoints
│   │   └── websocket.py        # WebSocket endpoints
│   │
│   ├── models/                 # Data models and schemas
│   │   └── schemas.py          # Pydantic schemas
│   │
│   ├── core/                   # Core utilities
│   │   ├── config.py           # Configuration settings
│   │   └── logger.py           # Logging setup
│   │
│   └── main.py                 # Application entry point
│
├── Dockerfile
├── requirements.txt
└── .env
```

## Features

### 1. **Agents** (`app/agents/`)
- **QuantAgent**: Technical analysis and quantitative metrics
- **SentimentAgent**: Market sentiment analysis
- **NewsAgent**: News-based insights
- **RiskAgent**: Risk assessment and management
- **PortfolioManager**: Portfolio decision-making

### 2. **Services** (`app/services/`)
- **MarketService**: Real-time market data fetching
- **GeminiService**: Google Gemini AI integration
- **WebSocketManager**: Real-time connection handling
- **CacheService**: Data caching for performance

### 3. **WebSocket** (`app/websocket/`)
- Real-time market updates
- Live trading notifications
- Client connection management

### 4. **Background Tasks** (`app/tasks/`)
- Async analysis processing
- Portfolio updates
- Scheduled analysis jobs

### 5. **API Routes** (`app/routes/`)
- Analysis endpoints
- WebSocket endpoints for real-time data

### 6. **Models** (`app/models/`)
- Pydantic schemas for request/response validation
- Data models for analysis results

### 7. **Core** (`app/core/`)
- Configuration management
- Logging system

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run with uvicorn
uvicorn app.main:app --reload

# Run with Docker
docker-compose up --build
```

## API Endpoints

### Analysis
- `GET /analyze/{ticker}` - Analyze a stock ticker
- `GET /` - Health check

### WebSocket
- `WS /ws/market/{ticker}` - Real-time market data stream

## Environment Variables

Create a `.env` file with:
```
GEMINI_API_KEY=your_key
MARKET_API_KEY=your_key
DATABASE_URL=your_url
REDIS_URL=your_url
```
