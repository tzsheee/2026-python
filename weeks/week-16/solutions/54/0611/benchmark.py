import json
import random
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort
from sorts_fast import bubble_sort as bubble_sort_fast, quick_sort as quick_sort_fast, merge_sort as merge_sort_fast


def make_data(n: int, seed: int = 42) -> list:
    if n < 0:
        raise ValueError(f"n must be non-negative, got {n}")
    random.seed(seed)
    return [random.randint(0, 10000) for _ in range(n)]


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sort_fns = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
        "bubble_sort_fast": bubble_sort_fast,
        "quick_sort_fast": quick_sort_fast,
        "merge_sort_fast": merge_sort_fast,
        "sorted_baseline": sorted,
    }

    results = {}
    for n in sizes:
        results[n] = {}
        for name, fn in sort_fns.items():
            timed_fn = timeit(fn)
            for _ in range(repeats):
                data = make_data(n)
                timed_fn(data)
            avg = sum(timed_fn.records) / len(timed_fn.records)
            results[n][name] = avg
            print(f"n={n:5d}  {name:15s}  {avg:.6f}s")
    return results


if __name__ == "__main__":
    print("Benchmarking sort algorithms...\n")
    data = run_benchmark()
    with open("results.json", "w") as f:
        json.dump(data, f, indent=2)
    print("\nSaved results.json")
