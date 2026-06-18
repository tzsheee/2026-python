"""0617 效能評估：linear vs binary search"""
import random
from timing import timeit
from search import linear_search, binary_search

N = 100000
raw_data = list(range(N))
random.shuffle(raw_data)
target = raw_data[-5]

sorted_data = sorted(raw_data)

@timeit(repeat=5)
def bench_linear():
    linear_search(raw_data, target)

@timeit(repeat=5)
def bench_binary():
    binary_search(sorted_data, target)

@timeit(repeat=5)
def bench_sort_and_binary():
    arr = sorted(raw_data)
    binary_search(arr, target)

print("=== 搜尋效能評估 (N=100000) ===")
bench_linear()
print(f"Linear Search:   {bench_linear.last_elapsed*1000:.3f} ms (avg of {len(bench_linear.records)})")
bench_binary()
print(f"Binary Search:   {bench_binary.last_elapsed*1000:.3f} ms (avg of {len(bench_binary.records)})")
bench_sort_and_binary()
print(f"Sort+Binary:     {bench_sort_and_binary.last_elapsed*1000:.3f} ms (avg of {len(bench_sort_and_binary.records)})")
