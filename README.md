# CollatzLyapunov

A Growth-Streak Enhanced Modular Lyapunov Function for the Collatz-Syracuse Map  
**Author:** Saeed Mohammadamini  
**Date:** March 31, 2025

---

This repository contains the complete implementation of a novel, drift-based Lyapunov-inspired function used to analyze average descent in Collatz-Syracuse trajectories. It combines modular penalties, a growth-streak heuristic, empirical simulation, and SAT-solver encoding to support reproducible experimentation and preliminary formal verification.

---

## 🧠 Project Overview

The Lyapunov-like function is defined as:

```
V(n) = log₂(n) + α(n mod 16) + β · growth_streak(n)
```

- `α(n mod 16)` is a modular penalty empirically tuned per residue class.
- `growth_streak(n)` penalizes consecutive appearances of growth-prone residues.
- `β = 0.7` was selected by grid search to optimize descent performance.

This formulation produces consistent **negative average drift** across thousands of seeds and enables **SAT-based formal encoding** of bounded descent conditions.

---

## 📁 Repository Structure

```
CollatzLyapunov/
│
├── src/                    # Core implementation modules
│   ├── lyapunov.py
│   ├── growth_streak.py
│   ├── penalties.py
│   ├── simulation.py
│   ├── beta_grid_search.py
│   ├── sat_encoder.py
│   └── utils.py
│
├── data/                   # Simulation and tuning outputs
│   ├── empirical_results.csv
│   ├── penalty_table.csv
│   └── beta_search_log.csv
│
├── notebooks/              # Jupyter notebooks for analysis
│   ├── validation.ipynb
│   └── visualization.ipynb
│
├── tests/                  # Unit tests
│   ├── test_lyapunov.py
│   ├── test_streak.py
│   └── test_sat_encoding.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Empirical Simulation
```bash
python src/simulation.py
```

This generates average `ΔV` values, positive step rates, and trajectory statistics over selected seeds.

### 3. Run SAT Encoding Example
```bash
python src/sat_encoder.py --n0 27 --steps 64
```

This produces SAT clauses verifying whether `V(n_i+1) < V(n_i)` holds over a bounded trajectory.

---

## 📊 Empirical Validation

- Tested seeds: 27 ≤ n₀ ≤ 10007  
- Metrics: average `ΔV`, positive step rate, min/max descent values  
- Result: ~90% steps show descent; global drift remains consistently negative.

Detailed tables are available in `data/empirical_results.csv`.

---

## 🧪 Reproducibility

- All penalty values (`α`) are provided in `data/penalty_table.csv`
- Growth-streak logic and β tuning scripts included
- SAT encoding routines are fully parameterized and documented
- Jupyter notebooks allow interactive exploration of results

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📎 Citation

If you use this code or methodology in your research, please cite:

```
@misc{mohammadamini2025collatzlyapunov,
  author    = {Saeed Mohammadamini},
  title     = {A Growth-Streak Enhanced Modular Lyapunov Function for the Collatz-Syracuse Map},
  year      = {2025},
  url       = {https://github.com/saeidmo/CollatzLyapunov}
}
```

---

## 💡 Future Work

- Formal drift bounds and stepwise descent guarantees  
- Extending SAT-based verification beyond 64 steps  
- Parameter derivation from theoretical Collatz residue dynamics  
- Validation against seeds with n₀ ≥ 10⁶  

---

## 🤝 Contributions

Feedback, pull requests, and research collaboration are welcome. Please open an issue or contact via GitHub.
