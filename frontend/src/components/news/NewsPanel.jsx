import Card from "../ui/Card";
import NewsCard from "./NewsCard";

function NewsPanel({ analysis }) {

  return (
    <Card>

      <h3>News</h3>

      {
        analysis?.news?.map(
          (
            item,
            index
          ) => (
            <NewsCard
              key={index}
              title={item}
            />
          )
        )
      }

    </Card>
  );
}

export default NewsPanel;