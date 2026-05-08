import { useState } from "react";

import MainLayout from "../layouts/MainLayout";

import Navbar from "../components/ui/Navbar";
import Button from "../components/ui/Button";

import HeroPanel from "../components/dashboard/HeroPanel";
import WatchList from "../components/dashboard/WatchList";
import MarketOverview from "../components/dashboard/MarketOverview";
import AIStatusPanel from "../components/dashboard/AIStatusPanel";

import StockChart from "../components/charts/StockChart";
import RSIChart from "../components/charts/RSIChart";
import MACDChart from "../components/charts/MACDChart";
import VolatilityChart from "../components/charts/VolatilityChart";

import NewsPanel from "../components/news/NewsPanel";

import MemoPanel from "../components/memo/MemoPanel";

import RiskPanel from "../components/risk/RiskPanel";

import { fetchStockAnalysis }
from "../hooks/useStockAnalysis";

function Dashboard() {

  const [ticker, setTicker] =
    useState("AAPL");

  const [analysis, setAnalysis] =
    useState(null);

  const analyzeStock = async () => {

    const data =
      await fetchStockAnalysis(
        ticker
      );

    setAnalysis(data);
  };

  return (
    <MainLayout>

      <Navbar />

      <div
        style={{
          marginBottom: "20px",
        }}
      >

        <input
          value={ticker}
          onChange={(e) =>
            setTicker(
              e.target.value
            )
          }
          style={{
            padding: "10px",
            marginRight: "10px",
          }}
        />

        <Button
          onClick={analyzeStock}
        >
          Analyze
        </Button>

      </div>

      <HeroPanel
        analysis={analysis}
      />

      <StockChart />

      <RSIChart
        analysis={analysis}
      />

      <MACDChart
        analysis={analysis}
      />

      <VolatilityChart
        analysis={analysis}
      />

      <NewsPanel
        analysis={analysis}
      />

      <RiskPanel
        analysis={analysis}
      />

      <MemoPanel
        analysis={analysis}
      />

      <WatchList />

      <MarketOverview />

      <AIStatusPanel />

    </MainLayout>
  );
}

export default Dashboard;