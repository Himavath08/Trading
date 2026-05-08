import Card from "../ui/Card";

function MACDChart({ analysis }) {

  return (
    <Card>

      <h3>MACD</h3>

      <h2>
        {analysis?.quant?.macd}
      </h2>

    </Card>
  );
}

export default MACDChart;