import Card from "../ui/Card";

function RSIChart({ analysis }) {

  return (
    <Card>

      <h3>RSI</h3>

      <h2>
        {analysis?.quant?.rsi}
      </h2>

    </Card>
  );
}

export default RSIChart;