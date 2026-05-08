import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import Card from "../ui/Card";

function StockChart() {

  const data = [
    { day: "Mon", value: 100 },
    { day: "Tue", value: 110 },
    { day: "Wed", value: 105 },
    { day: "Thu", value: 120 },
  ];

  return (
    <Card>

      <h3>Stock Chart</h3>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <LineChart data={data}>

          <XAxis dataKey="day" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="value"
            stroke="#2563eb"
          />

        </LineChart>

      </ResponsiveContainer>

    </Card>
  );
}

export default StockChart;