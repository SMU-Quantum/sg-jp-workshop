# QI4U in Singapore: Japan–Singapore Workshop on Applied Quantum Optimisation

This repository contains the tutorial material for the [Japan–Singapore Workshop on Applied Quantum Optimisation](https://a-star-engagementportal.glueup.com/event/japan-singapore-workshop-on-applied-quantum-optimisation-182741/), part of Tohoku University's [Quantum Infinity for You (QI4U) in Singapore](https://altema.is.tohoku.ac.jp/expo/singapore/en/) programme.

The workshop takes place in Singapore from **25–27 August 2026**. It combines lectures, hands-on tutorials, real quantum-hardware demonstrations, industry-inspired optimisation problems, and collaborative project work. The workshop is designed to connect participants from Singapore and Japan with practical quantum computing, artificial intelligence, and optimisation.

## Workshop context

Participants are introduced to:

- quantum annealing and gate-based quantum computing;
- Ising and QUBO formulations for combinatorial optimisation;
- hybrid variational algorithms such as VQE and QAOA;
- running optimisation models on cloud quantum systems, including D-Wave, Quantinuum, and IBM platforms;
- real-world applications in logistics, scheduling, manufacturing, healthcare, and related domains; and
- developing, evaluating, and presenting prototype solutions in groups.

### People and organisations

- **Prof. Hoong Chuin Lau** — Professor of Computer Science at [Singapore Management University](https://www.smu.edu.sg/). See his [SMU faculty profile](https://faculty.smu.edu.sg/profile/lau-hoong-chuin-631) and [research homepage](http://www.mysmu.edu/faculty/hclau/).
- **Prof. Masayuki Ohzeki** — Professor at [Tohoku University](https://www.tohoku.ac.jp/en/). See his [Tohoku University researcher profile](https://www.r-info.tohoku.ac.jp/en/d343b5fd84dd9eb2b5b385fccf39675d.html) and [researchmap profile](https://researchmap.jp/altema222).
- **Singapore Management University (SMU)** contributes the Singapore research and teaching context, including the SMU Quantum Optimisation Group showcase.
- **Tohoku University** leads the QI4U programme and contributes the Japanese quantum optimisation programme and research team.
- **A*STAR** hosts the event portal and the Singapore venue at the Innovis Building. The workshop is connected with the [National Quantum Computing Hub](https://nqch.sg), a national initiative involving the [A*STAR Institute of High Performance Computing](https://www.a-star.edu.sg/ihpc), the Centre for Quantum Technologies, and the National Supercomputing Centre Singapore.

### Event venue

Multi-Purpose Hall, Innovis Building #01-01<br>
2 Fusionopolis Way<br>
Singapore 138634

See the [official QI4U Singapore page](https://altema.is.tohoku.ac.jp/expo/singapore/en/) and the [A*STAR event page](https://a-star-engagementportal.glueup.com/event/japan-singapore-workshop-on-applied-quantum-optimisation-182741/) for the programme and event information.

## What this repository teaches

The materials use small, inspectable examples to demonstrate practical optimisation workflows. The quantum-annealing case study introduces the number partitioning problem, derives its QUBO formulation, and samples solutions with simulated quantum annealing (SQA) using the D-Wave Ocean SDK.

The gate-based notebooks demonstrate the following workflow:

1. define a classical optimisation problem;
2. obtain a classical reference solution;
3. formulate the problem as a quadratic program, QUBO, and Ising Hamiltonian;
4. build and optimise a parameterised quantum circuit;
5. sample and decode candidate bitstrings;
6. check feasibility, objective values, and optimality gaps; and
7. compare local simulation with a circuit transpiled and optionally executed on IBM Quantum hardware.

The examples emphasise that VQE and QAOA are hybrid, heuristic methods. Measurement returns samples from a distribution, not a guaranteed optimum, so the notebooks retain feasibility and objective information instead of reporting only the most frequent raw bitstring.

## Repository contents

| Path | Purpose |
| --- | --- |
| [`annealing/QI4U_Case_Study_slides.pdf`](annealing/QI4U_Case_Study_slides.pdf) | Slides for a quantum-annealing case study: number partitioning, QUBO formulation, sampling, and interpretation. |
| [`annealing/QI4U_Case_Study_code.ipynb`](annealing/QI4U_Case_Study_code.ipynb) | A 20–30 minute Google Colab exercise that solves a five-item number partitioning problem with Ocean SDK simulated quantum annealing. |
| [`qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb`](qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb) | Six-item knapsack solved with VQE and local Aer simulation. |
| [`qaoa_vqe_ibm_hardware/knapsack_qaoa.ipynb`](qaoa_vqe_ibm_hardware/knapsack_qaoa.ipynb) | The same six-item knapsack solved with QAOA and local Aer simulation. |
| [`qaoa_vqe_ibm_hardware/tsp_vqe.ipynb`](qaoa_vqe_ibm_hardware/tsp_vqe.ipynb) | Four-city travelling salesperson problem solved with a shallow VQE ansatz. |
| [`qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb`](qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb) | Four-city travelling salesperson problem solved with two-layer QAOA. |
| [`qaoa_vqe_ibm_hardware/ibm_hardware_qaoa.ipynb`](qaoa_vqe_ibm_hardware/ibm_hardware_qaoa.ipynb) | Local QAOA optimisation followed by IBM backend checks, pre-/post-transpilation comparison, per-qubit error inspection, and optional QPU submission. |
| [`qaoa_vqe_ibm_hardware/monitor_ibm_job.py`](qaoa_vqe_ibm_hardware/monitor_ibm_job.py) | Read-only command-line monitor for an existing IBM Runtime job. |
| [`custom_penalty/custom-penalty.ipynb`](custom_penalty/custom-penalty.ipynb) | Custom-penalty formulation for constrained binary optimisation. |
| [`requirements.txt`](requirements.txt) | Pinned Python dependencies for the workshop environment. |
| [`.env.example`](.env.example) | Safe template for IBM Quantum credentials; the real `.env` must remain local. |
| [`.gitignore`](.gitignore) | Excludes credentials, virtual environments, and generated local files. |



## Installation

The repository uses **Python 3.12** and a local `.venv` managed with [`uv`](https://docs.astral.sh/uv/). The pinned environment uses Qiskit and Qiskit IBM Runtime.

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

Check the environment:

```bash
python --version
uv pip check --python .venv/bin/python
```

The classical benchmark cells use IBM ILOG CPLEX through `qiskit-optimization`. If CPLEX is not available on a particular machine, the classical reference cells may need a locally available solver or a separate CPLEX installation/license.

## Launch JupyterLab

After activating the environment:

```bash
jupyter lab
```

Open a notebook from `annealing/CaseStudy`, `part01`, or `part02` and run its cells from top to bottom. The annealing case study is designed for Google Colab and installs its pinned `dwave-samplers` dependency in the setup cell. The gate-based simulator notebooks use Qiskit's local `AerSimulator`, so they do not require cloud credentials.

If `jupyter lab` reports `jupyter-lab` not found, reinstall into the active environment and launch the executable directly:

```bash
source .venv/bin/activate
uv pip install --python .venv/bin/python -r requirements.txt
./.venv/bin/jupyter lab
```

On Windows PowerShell, use `.venv\Scripts\Activate.ps1`, `.venv\Scripts\python.exe`, and `.venv\Scripts\jupyter.exe`.

## Suggested teaching sequence in Gate-based

1. Start with [`qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb`](qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb) or [`qaoa_vqe_ibm_hardware/knapsack_qaoa.ipynb`](qaoa_vqe_ibm_hardware/knapsack_qaoa.ipynb) to establish the optimisation-to-QUBO workflow.
2. Compare the VQE and QAOA notebooks on the shared knapsack instance.
3. Use [`qaoa_vqe_ibm_hardware/tsp_vqe.ipynb`](qaoa_vqe_ibm_hardware/tsp_vqe.ipynb) and [`qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb`](qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb) to extend the workflow to a four-city routing problem.
4. Study [`custom_penalty/custom-penalty.ipynb`](custom_penalty/custom-penalty.ipynb) to see how constraints can be encoded without slack variables, once `custom_penalty` is available.
5. Use [`qaoa_vqe_ibm_hardware/ibm_hardware_qaoa.ipynb`](qaoa_vqe_ibm_hardware/ibm_hardware_qaoa.ipynb) for the real-hardware demonstration.
6. Continue with group work: formulate a problem, choose a classical or quantum approach, run experiments, analyse limitations, and prepare a final presentation.

## IBM Quantum hardware demonstration

The hardware notebook is deliberately opt-in. It first optimises the QAOA parameters locally, then separates hardware preparation from submission:

1. **Local optimisation:** run the two-layer QAOA circuit against Aer.
2. **Connect and pre-flight:** set `USE_IBM_BACKEND = True`. The notebook checks reachable operational QPUs, confirms the selected backend, reports pending jobs, and recommends the least-busy eligible backend. It checks `service.usage()` when the active channel and plan expose that method.
3. **Before transpilation:** inspect the logical circuit, its depth, and its number of qubits.
4. **Transpile only:** set `OPTIMIZATION_LEVEL` to `0`, `1`, `2`, or `3`. Set `SHOW_ALL_OPTIMIZATION_LEVELS = True` to display all four transpiled circuits without submitting anything.
5. **Calibration/layout inspection:** compare per-qubit readout and `sx` gate errors, with the physical qubits selected by the transpiler highlighted. This supports a discussion of layout, connectivity, and whether noisy qubits were avoided.
6. **Submit separately:** set `SUBMIT_HARDWARE_JOB = True` only in the dedicated submission cell. The notebook submits a bounded number of shots using IBM Runtime V2 `Sampler`.
7. **Monitor and analyse:** use the notebook monitor or the command-line monitor below, then compare raw counts, feasible-shot rate, selected feasible solution, and objective value.

### Credentials

Copy the template only if `.env` does not already exist:

```bash
cp .env.example .env
```

Fill in the local file without committing or sharing it:

```text
IBM_QUANTUM_TOKEN=<your IBM Quantum API token>
IBM_QUANTUM_INSTANCE=<your IBM Quantum instance or CRN>
IBM_BACKEND=<optional operational backend name>
```

The notebook reads these values at runtime. It never prints the token. The repository's `.gitignore` excludes `.env`.

### Pre-flight API note

IBM's newer `qiskit-ibm-catalog` methods—`usage()`, `backends()`, `backend()`, and `least_busy()`—are documented for the Qiskit Functions service. The hardware notebook uses IBM Runtime `QiskitRuntimeService`, so it uses the corresponding Runtime service methods instead. This is important because the current repository is pinned to the Qiskit 1.x/Runtime 0.40 stack, while the current catalog client requires the newer Qiskit 2.x/Runtime stack. Installing the catalog client into this environment would upgrade the workshop dependencies; use a separate environment if Qiskit Functions are added later.

For the configured `ibm_quantum_platform` account, Runtime capacity may report as unavailable because `service.usage()` is plan/channel dependent. The notebook handles that case explicitly and still performs backend-access, operational-status, and least-busy checks before submission.

### Monitor an existing job

```bash
python part01/monitor_ibm_job.py <IBM_JOB_ID> --interval 30
```

Use `--once` for a single read-only status check:

```bash
python part01/monitor_ibm_job.py <IBM_JOB_ID> --once
```

Runtime V2 exposes job states such as `QUEUED`, `RUNNING`, `DONE`, and `CANCELLED`. Runtime V2 job objects do not generally expose an exact queue-position method, so the monitor reports queue position only when the installed API provides it.

## Safety and reproducibility notes

- Do not place IBM Quantum tokens in notebooks, source files, commits, or public issues.
- Keep `SUBMIT_HARDWARE_JOB = False` while teaching circuit construction, pre-flight checks, and transpilation.
- Hardware jobs are remote and may be queued, cancelled, or affected by calibration changes.
- Hardware distributions will not necessarily match ideal simulation. Report raw counts, feasibility, selected feasible solutions, and objective values.
- TSP and knapsack examples are intentionally small so that students can inspect the model, circuit, transpilation, and measurement results in one session.
- Random seeds, circuit depths, and optimiser settings are included in the notebooks to make the workshop runs easier to reproduce.

## Further information

- [QI4U in Singapore — Quantum Universe EXPO](https://altema.is.tohoku.ac.jp/expo/singapore/en/)
- [Japan–Singapore Workshop event page — A*STAR / Glue Up](https://a-star-engagementportal.glueup.com/event/japan-singapore-workshop-on-applied-quantum-optimisation-182741/)
- [Singapore Management University](https://www.smu.edu.sg/)
- [A*STAR](https://www.a-star.edu.sg/)
- [National Quantum Computing Hub](https://nqch.sg/)
- [IBM Quantum Runtime documentation](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-runtime-primitives)
