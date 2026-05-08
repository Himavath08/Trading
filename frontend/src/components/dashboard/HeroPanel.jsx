import Card from "../ui/Card";

function HeroPanel({ analysis }) {

  if (!analysis) return null;

  return (
    <Card>

      <h1>
        {analysis.ticker}
      </h1>

      <h2>
        Decision:
        {" "}
        {analysis.decision}
      </h2>

      <p>
        Risk:
        {" "}
        {analysis.risk}
      </p>

    </Card>
  );
}

export default HeroPanel;