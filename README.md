# QI4U in Singapore: Japan–Singapore Workshop on Applied Quantum Optimisation

This repository contains the tutorial material for the [Japan–Singapore Workshop on Applied Quantum Optimisation](https://a-star-engagementportal.glueup.com/event/japan-singapore-workshop-on-applied-quantum-optimisation-182741/), part of Tohoku University's [Quantum Infinity for You (QI4U) in Singapore](https://altema.is.tohoku.ac.jp/expo/singapore/en/) programme.

It combines lectures, hands-on tutorials, real quantum-hardware demonstrations, industry-inspired optimisation problems, and collaborative project work. The workshop is designed to connect participants from Singapore and Japan with practical quantum computing, artificial intelligence, and optimisation.

## Workshop context

Participants are introduced to:

- quantum annealing and gate-based quantum computing;
- Ising and QUBO formulations for combinatorial optimisation;
- hybrid variational algorithms such as VQE and QAOA;
- running optimisation models on cloud quantum systems, including D-Wave, Quantinuum, and IBM platforms;
- real-world applications in logistics, scheduling, manufacturing, healthcare, and related domains; and
- developing, evaluating, and presenting prototype solutions in groups.


## Tutorial tracks

The workshop material is divided into two independent tracks. Each track has its own guide, notebook index, suggested teaching sequence, and service-specific notes.

Before proceeding to these tutorials, complete the environment setup described below.

| Track | Guide | Topics |
| --- | --- | --- |
| Gate-based quantum computing | [Gate-based tutorial guide](gate_based/README.md) | QUBO and Ising formulations, VQE, QAOA, custom penalties, local Aer simulation, and optional IBM Quantum hardware execution |
| Quantum annealing | [Quantum-annealing tutorial guide](annealing/README.md) | Number partitioning, traffic-congestion reduction, portfolio optimisation, simulated annealing/SQA, and optional D-Wave QPU execution |

## Installation

The repository uses **Python 3.12** and a local `.venv` managed with [`uv`](https://docs.astral.sh/uv/). The root [`requirements.txt`](requirements.txt) installs the dependencies for both tutorial tracks by combining the manifests under [`gate_based/`](gate_based/requirements.txt) and [`annealing/`](annealing/requirements.txt). Use the root manifest for the supported workshop environment.

### macOS/Linux

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install --python .venv/bin/python -r requirements.txt
```

### Windows PowerShell

```powershell
uv venv --python 3.12 .venv
.venv\Scripts\Activate.ps1
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
```

Check the environment on macOS/Linux:

```bash
python --version
uv pip check --python .venv/bin/python
```

On Windows PowerShell:

```powershell
python --version
uv pip check --python .venv\Scripts\python.exe
```

The classical benchmark cells in the gate-based track use IBM ILOG CPLEX through `qiskit-optimization`. If CPLEX is unavailable on a particular machine, those cells require a locally available alternative solver or a separate CPLEX installation and licence.

## Launch JupyterLab

After activating the environment, start JupyterLab from the repository root:

```bash
jupyter lab
```

Open a notebook under `annealing/` or `gate_based/` and run its cells from top to bottom. Some notebooks contain a `%pip install` cell for Google Colab; it is harmless but unnecessary after installing the root requirements locally.

If `jupyter lab` reports `jupyter-lab` not found, reinstall the requirements into the active environment and launch the executable directly:

```bash
source .venv/bin/activate
uv pip install --python .venv/bin/python -r requirements.txt
./.venv/bin/jupyter lab
```

On Windows PowerShell, use `.venv\Scripts\Activate.ps1`, `.venv\Scripts\python.exe`, and `.venv\Scripts\jupyter.exe`.

## General safety and reproducibility notes

- Do not place IBM Quantum or D-Wave tokens in notebooks, source files, commits, or public issues.
- Keep remote-hardware submission disabled until the relevant pre-flight checks have been completed.
- Remote jobs may be queued, cancelled, or affected by calibration changes.
- Hardware distributions will not necessarily match ideal or simulated results. Retain feasibility and objective information when interpreting samples.
- Internet access is required when a notebook downloads map data, market data, or connects to a cloud service.

Track-specific setup and execution details are in the [gate-based guide](gate_based/README.md) and [quantum-annealing guide](annealing/README.md).

## Further information

- [QI4U in Singapore — Quantum Universe EXPO](https://altema.is.tohoku.ac.jp/expo/singapore/en/)
- [Japan–Singapore Workshop event page — A*STAR / Glue Up](https://a-star-engagementportal.glueup.com/event/japan-singapore-workshop-on-applied-quantum-optimisation-182741/)
- [Singapore Management University](https://www.smu.edu.sg/)
- [A*STAR](https://www.a-star.edu.sg/)
- [National Quantum Computing Hub](https://nqch.sg/)
