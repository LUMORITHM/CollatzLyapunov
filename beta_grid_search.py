import csv
from empirical_validation import analyze_trajectory
from typing import List

def beta_grid_search(
    seeds: List[int],
    beta_values: List[float],
    max_steps: int = 1000,
    output_file: str = "data/beta_search_log.csv"
) -> None:
    """
    Performs a grid search over beta values to evaluate average ΔV descent metrics.

    Parameters:
        seeds (List[int]): List of initial seed values to test.
        beta_values (List[float]): List of beta values to test.
        max_steps (int): Maximum number of trajectory steps per seed. Default is 1000.
        output_file (str): Path to save the grid search result as a CSV file. Default is "data/beta_search_log.csv".
    """
    try:
        with open(output_file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["beta", "seed", "avg_delta_V", "pos_rate", "max_delta_V", "min_delta_V"])

            for beta in beta_values:
                for seed in seeds:
                    result = analyze_trajectory(seed, beta=beta, max_steps=max_steps)
                    writer.writerow([
                        beta,
                        result["n0"],
                        result["avg_delta_V"],
                        result["pos_rate"],
                        result["max_delta_V"],
                        result["min_delta_V"]
                    ])
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

if __name__ == "__main__":
    # Define search range
    beta_values = [round(0.1 * i, 2) for i in range(3, 12)]  # 0.3 to 1.1
    seeds = [27, 31, 95, 703, 10007]  # Representative seeds

    beta_grid_search(seeds, beta_values)
