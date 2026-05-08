function Navbar() {

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        padding: "20px",
        background: "#0f172a",
        borderRadius: "12px",
        marginBottom: "20px",
      }}
    >
      <h2>
        AI Financial Intelligence
      </h2>

      <div>
        Market: OPEN
      </div>
    </div>
  );
}

export default Navbar;