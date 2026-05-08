import { create } from "zustand";

const useStockStore = create((set) => ({
  analysis: null,

  setAnalysis: (data) =>
    set({
      analysis: data,
    }),
}));

export default useStockStore;