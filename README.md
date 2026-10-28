# Stock Covariance & Correlation Calculator

This workspace contains a Python analysis for stock return behavior across major market indices and bank stocks. The project computes daily, weekly, and monthly log and percentage returns, then summarizes them with sample means, covariance matrices, and correlation matrices.

## Actual project files

- `calculate.py` — Main script that reads the bank-stock dataset and prints daily, weekly, and monthly return summaries for the selected columns.
- `matrix_operations_utility.py` — Shared functions for formatting output and calculating means, covariance, and correlation matrices.
- `requirement.txt` — Python dependencies needed to run the analysis.
- `sample data/indices-july2016.csv` — Input stock-price data used by `calculate.py`.
- `sample data/indeces-close-jan3-jan31-2017.xlsx` — Additional market-index workbook present in the workspace.

## What the script does

`calculate.py` reads `sample data/indices-july2016.csv`, sorts the date index, and analyzes the following selected bank stocks:

- BAC
- BNS
- C
- GS
- JPM
- MS
- TD
- USB
- WFC

It calculates:

- Daily log returns
- Daily percentage returns
- Weekly log and percentage returns
- Monthly log and percentage returns
- Sample means
- Covariance matrices
- Correlation matrices

All results are printed to the console.

## Setup

Create a virtual environment and install the pinned dependencies from `requirement.txt`.

In PowerShell from the project root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirement.txt
```

If activation is blocked in PowerShell, run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirement.txt
```

## Run

```powershell
python calculate.py
```

This script expects to be run from the repository root so it can resolve `sample data\indices-july2016.csv` correctly.
