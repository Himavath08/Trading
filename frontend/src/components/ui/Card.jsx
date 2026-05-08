function Card({ children }) {

  return (
    <div
      style={{
        background: "#0f172a",
        padding: "20px",
        borderRadius: "12px",
        marginBottom: "20px",
      }}
    >
      {children}
    </div>
  );
}

export default Card;