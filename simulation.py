import csv
from typing import List
from empirical_validation import analyze_trajectory

def run_simulation(
    seeds: List[int],
    beta: float = 0.7,
    max_steps: int = 1000,
    output_file: str = "data/empirical_results.csv"
) -> None:
    """
    Runs empirical validation on a list of seeds and saves results to a CSV file.

    Parameters:
        seeds (List[int]): List of initial seed values to test.
        beta (float): Beta value for Lyapunov function.
        max_steps (int): Max number of trajectory steps per seed.
        output_file (str): Output path for CSV.
    """
    try:
        with open(output_file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["seed", "avg_delta_V", "pos_rate", "max_delta_V", "min_delta_V"])

            for seed in seeds:
                result = analyze_trajectory(seed, beta=beta, max_steps=max_steps)
                writer.writerow([
                    result["n0"],
                    result["avg_delta_V"],
                    result["pos_rate"],
                    result["max_delta_V"],
                    result["min_delta_V"]
                ])

        print(f"✅ Simulation completed and saved to {output_file}")
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
    except PermissionError as e:
        print(f"❌ Permission error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    seeds = list(range(27, 10008, 100))  # Sampled over the same interval from the paper
    run_simulation(seeds)
