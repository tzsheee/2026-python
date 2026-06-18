import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path) as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise ValueError(f"expected dict, got {type(raw).__name__}")
    return {int(k): v for k, v in raw.items()}


def plot_results(results: dict, out_path: str) -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    sizes = sorted(results.keys())
    algorithms = set()
    for v in results.values():
        algorithms.update(v.keys())

    plt.figure(figsize=(10, 6))
    for algo in sorted(algorithms):
        times = [results[n][algo] for n in sizes]
        plt.plot(sizes, times, marker="o", label=algo)

    plt.xlabel("Data size (n)")
    plt.ylabel("Average time (s)")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == "__main__":
    data = load_results("results.json")
    os.makedirs("assets", exist_ok=True)
    plot_results(data, "assets/benchmark.png")
    print("Saved assets/benchmark.png")
