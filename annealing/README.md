# Quantum-annealing tutorials

This track introduces the complete annealing workflow: express an optimisation objective and its constraints with binary variables, construct a QUBO, sample candidate solutions, decode them in the original problem domain, and evaluate feasibility and solution quality.

The materials progress from a small, inspectable number-partitioning example to applied routing and portfolio problems. Local samplers are available for every topic; the portfolio notebook also contains an optional D-Wave quantum processing unit (QPU) section.

For the supported Python 3.12 environment and JupyterLab instructions, see the [repository README](../README.md#installation). This track's package manifest is [`requirements.txt`](requirements.txt) and is included by the root environment.

## Contents

| Path | Purpose |
| --- | --- |
| [`CaseStudy/QI4U_Case_Study_slides.pdf`](CaseStudy/QI4U_Case_Study_slides.pdf) | Slides introducing quantum annealing, number partitioning, QUBO formulation, sampling, and interpretation. |
| [`CaseStudy/QI4U_Case_Study_code.ipynb`](CaseStudy/QI4U_Case_Study_code.ipynb) | A short exercise that derives a five-item number-partitioning QUBO and solves it with simulated quantum annealing (SQA). |
| [`Handson1/QI4U_Handson1_Traffic_Congestion_Reduction.ipynb`](Handson1/QI4U_Handson1_Traffic_Congestion_Reduction.ipynb) | Route assignment around Singapore Management University, including OpenStreetMap road data, congestion and one-route-per-car penalties, QUBO construction, local simulated annealing, and route visualisation. |
| [`Handson2/QI4U_Handson2_Portfolio_Optimization.ipynb`](Handson2/QI4U_Handson2_Portfolio_Optimization.ipynb) | Portfolio optimisation with market data, return/budget/asset-class/volatility terms, local simulated annealing, optional D-Wave QPU sampling, and backtesting. |

## Suggested teaching sequence

1. Begin with the case-study slides and notebook. Derive the number-partitioning QUBO by hand, inspect its matrix, sample it with SQA, and decode the best bitstring.
2. Continue with Hands-on 1. Build a road-network routing problem from map data, translate congestion and route-choice constraints into a QUBO, and visualise the selected routes.
3. Continue with Hands-on 2. Encode fractional asset weights with binary variables, combine several penalty terms, assess feasible samples, and compare the resulting portfolio in a backtest.
4. If D-Wave Leap access is available, run the optional QPU section in Hands-on 2 and compare its samples with the local simulated-annealing result.

## Execution notes

### Case study

The case-study notebook runs locally after the dependencies are installed. Its setup cell also installs the pinned `dwave-samplers` version for Google Colab users.

### Hands-on 1: traffic-congestion reduction

The notebook downloads OpenStreetMap road data through OSMnx, so its map-loading cells require internet access. Optimisation uses `SimulatedAnnealingSampler` locally and does not require a D-Wave account.

### Hands-on 2: portfolio optimisation

The notebook downloads historical market data with `yfinance` and stores CSV files in a local `cache/` directory. The first run for a date range requires internet access; subsequent runs can reuse the cached data.

The main simulated-annealing workflow is local. The section titled “Solving it on a real quantum annealer (QPU)” is optional and requires a D-Wave Leap API token. Supply the token through the `DWAVE_API_TOKEN` environment variable or Google Colab user data when possible. If neither is present, the notebook prompts for it without echoing the value.

macOS/Linux:

```bash
export DWAVE_API_TOKEN=<your D-Wave Leap API token>
```

Windows PowerShell:

```powershell
$env:DWAVE_API_TOKEN = '<your D-Wave Leap API token>'
```

Do not save the token in the notebook or commit it to the repository.

## Reproducibility and interpretation

- Annealing methods return samples rather than a guaranteed optimum. Inspect constraint feasibility and the decoded objective, not only the lowest reported QUBO energy.
- The case study fixes its NumPy seed. The applied notebooks may still vary because samplers, downloaded data, and remote hardware can change between runs.
- Market-data results depend on the requested dates and the data returned by Yahoo Finance.
- A D-Wave QPU run can differ from local simulated annealing because of embedding, hardware noise, calibration, and sampling variation.
