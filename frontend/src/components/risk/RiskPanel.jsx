import Card from "../ui/Card";
import RiskGauge from "./RiskGauge";

function RiskPanel({ analysis }) {

  return (
    <Card>

      <h3>Risk Analysis</h3>

      <RiskGauge
        risk={analysis?.risk}
      />

    </Card>
  );
}

export default RiskPanel;