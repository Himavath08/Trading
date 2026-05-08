# Trading Application

A comprehensive multi-agent trading system with quantitative analysis, sentiment analysis, and risk management capabilities.

## Project Structure

```
Trading/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── quant_agent.py
│   │   │   ├── sentiment_agent.py
│   │   │   ├── risk_agent.py
│   │   │   └── portfolio_manager.py
│   │   │
│   │   ├── services/
│   │   │   ├── news_service.py
│   │   │   └── llm_service.py
│   │   │
│   │   ├── routes/
│   │   │   └── analysis.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
│
└── README.md
```

## Components

### Backend
- **Agents**: Specialized AI agents for different trading tasks
  - `quant_agent.py` - Quantitative analysis
  - `sentiment_agent.py` - Market sentiment analysis
  - `risk_agent.py` - Risk management
  - `portfolio_manager.py` - Portfolio management

- **Services**: Core business logic and external integrations
  - `news_service.py` - News data fetching and processing
  - `llm_service.py` - Large Language Model integration

- **Routes**: API endpoints
  - `analysis.py` - Trading analysis endpoints

- **Core**: Configuration and utilities
  - `config.py` - Application configuration

### Frontend
- React-based user interface
- Located in `frontend/src/`

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)

### Using Docker Compose
```bash
docker-compose up
```

This will start:
- Backend API on `http://localhost:8000`
- Frontend on `http://localhost:3000`
- PostgreSQL database on `localhost:5432`

### Local Development

#### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## Environment Variables

Create a `.env` file in the `backend/` directory with required configurations.

## License

MIT
