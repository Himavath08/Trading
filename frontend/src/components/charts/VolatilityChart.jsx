import Card from "../ui/Card";

function VolatilityChart({
  analysis,
}) {

  return (
    <Card>

      <h3>Volatility</h3>

      <h2>
        {
          analysis?.quant
            ?.volatility
        }
      </h2>

    </Card>
  );
}

export default VolatilityChart;