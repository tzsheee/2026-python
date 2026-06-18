# AI_LOG

## Task 1 — timeit 裝飾器

### 我問 AI 什麼

請幫我用 TDD 方式實作 timeit 裝飾器，規格在 README.md 第 28~36 行。

### AI 反問我什麼 / 我怎麼回答

| AI 反問 | 我回答 |
|---|---|
| 函式簽名與回傳型別？ | 帶 repeat 參數預設 3；回傳值不變；functools.wraps |
| repeat 合法範圍？ | repeat ≥ 1；float 照規格不額外檢查 |
| 例外行為 — 何時 raise？ | 呼叫被裝飾函式時才 raise |
| edge cases 要測哪些？ | repeat=1、字串傳入、副作用、無 print 汙染、回傳值、metadata |
| 驗收標準 — 紅燈定義？ | 全部 fail |

### AI 給了什麼

給了一份 6 個 test case 的測試骨架，以及完整的 timeit 實作（含 repeat 參數、records、last_elapsed）。

### 我改了什麼

維持 AI 提供的測試與實作，但選擇例外在「呼叫函式時」才 raise（非 fail fast 的裝飾時檢查）。

---

## Task 2 — linear_search & binary_search

### 我問 AI 什麼

請幫我用 TDD 實作 linear_search 與 binary_search，規格見 README.md 第 40~47 行。

### AI 反問我什麼 / 我怎麼回答

| AI 反問 | 我回答 |
|---|---|
| 函式簽名與回傳型別？ | 兩者均為 (data: list, target) -> int；找不到回 -1 |
| 邊界條件 — data 長度 0、1？ | 空 list 回 -1；單元素 list 比對後回 0 或 -1 |
| 例外行為 — 非 list 或 target=None？ | Duck typing，讓 Python 自己炸 |
| edge cases 要測哪些？ | 空 list、單元素、重複值（linear 回第一個）、最左/最右、奇偶長度、找不到夾擊 |
| 驗收標準？ | 全部 fail 才算紅 |

### AI 給了什麼

給了 16 個 test case 涵蓋 edge case，以及 linear_search（逐一比對）與 binary_search（標準二分）實作。

### 我改了什麼

維持 AI 提供的實作，無修改。

---

## 效能評估

```
Linear Search:   2.748 ms (avg of 5)
Binary Search:   0.003 ms (avg of 5)
Sort+Binary:     10.392 ms (avg of 5)
```

結論：資料已排序時 Binary 快 ~900 倍；未排序且只搜一次時 Linear 反而划算。
