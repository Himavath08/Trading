import api from "../services/api";

export const fetchStockAnalysis = async (
  ticker
) => {

  const response = await api.get(
    `/analyze/${ticker}`
  );

  return response.data;
};