# AI_LOG

日期：2026-06-10

提示詞（逐字記錄）：
```
Implement a Python function `digit_root(n: int) -> int` that returns the digital root
of `n` by repeatedly summing its digits until a single-digit result remains.

Requirements:
- If `n < 1`, raise `ValueError("n must be >= 1")` (message must match exactly).
- `n` is an integer in range 1..2_000_000_000. One-digit inputs return themselves.
- Do not use `input()` or `print()`; provide only the function in `digit_root.py`.
- Prefer an efficient implementation (formula or loop is fine).
```

實作摘要：
- 新增 `digit_root.py`，實作採用數學同餘公式 `1 + (n-1) % 9` 以取得數字根，並加入輸入型別與範圍檢查（`TypeError` 若非 int，`ValueError` 若 n < 1）。

測試：
- 新增 `test_digit_root.py`（basic / edge / invalid cases），並在 solutions 目錄下執行：

```bash
cd weeks/week-16/solutions/0610
python -m unittest -v
```

結果：3 tests OK

下一步建議：
- 若要提交，請 commit 三個檔案（`digit_root.py`, `test_digit_root.py`, `AI_LOG.md`）到你的分支，commit 訊息可用：
  - `test: add failing tests for digit root`（若先 only tests）
  - `feat: implement digit root`（實作完成時）

備註：本檔為學生交作業用的 AI 日誌，已包含提示詞逐字記錄與測試紀錄。
