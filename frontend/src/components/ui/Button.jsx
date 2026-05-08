function Button({
  children,
  onClick,
}) {

  return (
    <button
      onClick={onClick}
      style={{
        background: "#2563eb",
        color: "white",
        border: "none",
        padding: "10px 20px",
        borderRadius: "10px",
        cursor: "pointer",
      }}
    >
      {children}
    </button>
  );
}

export default Button;