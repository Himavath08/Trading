# Frontend Architecture

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── ui/              # Reusable UI components
│   │   │   ├── Button.jsx   # Button variants
│   │   │   ├── Card.jsx     # Card container
│   │   │   ├── Loader.jsx   # Loading spinner
│   │   │   └── Navbar.jsx   # Navigation bar
│   │   │
│   │   ├── dashboard/       # Dashboard components
│   │   │   ├── HeroPanel.jsx
│   │   │   ├── WatchList.jsx
│   │   │   ├── MarketOverview.jsx
│   │   │   └── AIStatusPanel.jsx
│   │   │
│   │   ├── charts/          # Chart components
│   │   │   ├── StockChart.jsx
│   │   │   ├── RSIChart.jsx
│   │   │   ├── MACDChart.jsx
│   │   │   └── VolatilityChart.jsx
│   │   │
│   │   ├── news/            # News components
│   │   │   ├── NewsCard.jsx
│   │   │   └── NewsPanel.jsx
│   │   │
│   │   ├── memo/            # Trading memo components
│   │   │   ├── MemoCard.jsx
│   │   │   └── MemoPanel.jsx
│   │   │
│   │   └── risk/            # Risk assessment components
│   │       ├── RiskGauge.jsx
│   │       └── RiskPanel.jsx
│   │
│   ├── pages/               # Page components
│   │   └── Dashboard.jsx    # Main dashboard page
│   │
│   ├── layouts/             # Layout components
│   │   └── MainLayout.jsx   # Main app layout with nav & footer
│   │
│   ├── hooks/               # Custom React hooks
│   │   └── useStockAnalysis.js
│   │
│   ├── services/            # API services
│   │   └── api.js           # Axios API client
│   │
│   ├── store/               # State management
│   │   └── stockStore.js    # Zustand store
│   │
│   ├── styles/              # Global styles
│   │   └── globals.css      # Tailwind + custom styles
│   │
│   ├── App.jsx              # Root component
│   └── main.jsx             # React entry point
│
├── public/                  # Static assets
├── Dockerfile               # Docker configuration
├── package.json             # Dependencies
├── tailwind.config.js       # Tailwind CSS config
├── postcss.config.js        # PostCSS config
├── vite.config.js           # Vite config
└── README.md
```

## Technologies

- **React 19** - UI framework
- **Vite** - Build tool
- **Tailwind CSS** - Utility-first CSS
- **Axios** - HTTP client
- **Zustand** - State management
- **ESLint** - Code quality

## Features

### Components
- **UI**: Reusable Button, Card, Loader, Navbar
- **Dashboard**: Hero panel, watchlist, market overview, AI status
- **Charts**: Stock price, RSI, MACD, Volatility
- **News**: News cards and panels
- **Memos**: Trading notes with priority levels
- **Risk**: Risk gauge and assessment metrics

### Hooks
- `useStockAnalysis` - Stock analysis custom hook

### Services
- Centralized API client with error handling
- Stock analysis, market data, portfolio management

### State Management
- Zustand store for reactive state
- Stocks, portfolio, selected ticker

### Styling
- Tailwind CSS with custom config
- Global animations and utilities
- Responsive design patterns

## Getting Started

```bash
# Install dependencies
npm install

# Add Tailwind CSS
npm install -D tailwindcss postcss autoprefixer

# Start development server
npm run dev

# Build for production
npm run build
```

## Environment Variables

Create `.env.local`:
```
VITE_API_URL=http://localhost:8000/api
```

## API Integration

All API calls go through the centralized `api.js` service:
- Health check
- Stock analysis
- Market data
- Portfolio management
