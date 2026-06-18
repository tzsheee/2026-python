# AI_LOG

## Stage 1 — timeit 裝飾器

**我問 AI 什麼**：「do stage1,拆 ≥3 個 test case（含 ≥1 個 edge case)」

**AI 給了什麼**：先問了函式簽名、例外行為、edge case、驗收標準等檢查表問題，確認後給了 6 個 test case（含例外仍記錄、無參數回傳 None、多次呼叫累積等 edge case），以及 timeit 實作。

**我改了什麼**：AI 給的測試中 `add(1)` 少傳參數導致 TypeError，我指出後 AI 修正為 `add(1, 2)`。其餘照用。

## Stage 2 — 三種排序與 benchmark

**我問 AI 什麼**：「go」（進入 Stage 2）

**AI 給了什麼**：先問了邊界條件、例外行為、edge case、驗收標準，確認後給了 7 個共用 test case（含 empty、single、already sorted、reverse sorted、all equal、random、input not mutated、uncomparable），以及 bubble/quick/merge 三種排序實作與 benchmark.py。

**我改了什麼**：照單全收，無修改。benchmark 執行產出 results.json 後自動作 commit。

## Stage 3 — Cython 加速

**我問 AI 什麼**：「Cython 化」

**AI 給了什麼**：先裝 Cython，寫了 sorts_fast.pyx 和 setup.py，編譯成功。加速版加入 test_sorts.py 的 SORT_FUNCTIONS（red 階段），重建 .pyd 後測試全綠。

**我改了什麼**：無。確認加速比後 commit。

## Stage 4 — 繪圖與報告

**我問 AI 什麼**：「go」（進入 Stage 4）

**AI 給了什麼**：寫了 test_plot.py（3 個測試：load_results 回傳 dict、key 為 int、PNG 存在且非空）、plot.py（加入 matplotlib.use("Agg")、自動建立 assets/、log scale 折線圖）。

**我改了什麼**：無。

## Stage 5 — 安全性自掃

**我問 AI 什麼**：「go」（進入 Stage 5）

**AI 給了什麼**：掃了 Stage 1-4 所有程式碼，找出 3 個適用問題並寫成測試（test_security.py），修復後全綠。

**我改了什麼**：無。照流程 commit test→feat。
