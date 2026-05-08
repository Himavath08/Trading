import Card from "../ui/Card";
import MemoCard from "./MemoCard";

function MemoPanel({ analysis }) {

  return (
    <Card>

      <h3>AI Investment Memo</h3>

      <MemoCard
        memo={analysis?.memo}
      />

    </Card>
  );
}

export default MemoPanel;