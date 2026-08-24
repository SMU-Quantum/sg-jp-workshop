# Gate-based quantum computing tutorials

This track demonstrates a practical optimisation workflow with gate-based quantum algorithms:

1. define a classical optimisation problem;
2. obtain a classical reference solution;
3. formulate the problem as a quadratic program, QUBO, and Ising Hamiltonian;
4. build and optimise a parameterised quantum circuit;
5. sample and decode candidate bitstrings;
6. check feasibility, objective values, and optimality gaps; and
7. compare local simulation with a circuit transpiled and optionally executed on IBM Quantum hardware.

VQE and QAOA are hybrid, heuristic methods. Measurement returns samples from a distribution, not a guaranteed optimum, so the notebooks retain feasibility and objective information instead of reporting only the most frequent raw bitstring.

For the supported Python 3.12 environment and JupyterLab instructions, see the [repository README](../README.md#installation). This track's package manifest is [`requirements.txt`](requirements.txt) and is included by the root environment.

## Contents

| Path | Purpose |
| --- | --- |
| [`part01_qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb`](part01_qaoa_vqe_ibm_hardware/knapsack_vqe.ipynb) | Six-item knapsack solved with VQE and local Aer simulation. |
| [`part01_qaoa_vqe_ibm_hardware/knapsack_qaoa_guided.ipynb`](part01_qaoa_vqe_ibm_hardware/knapsack_qaoa_guided.ipynb) | Guided treatment of the same six-item knapsack with QAOA and local Aer simulation. |
| [`part01_qaoa_vqe_ibm_hardware/tsp_vqe.ipynb`](part01_qaoa_vqe_ibm_hardware/tsp_vqe.ipynb) | Four-city travelling salesperson problem solved with a shallow VQE ansatz. |
| [`part01_qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb`](part01_qaoa_vqe_ibm_hardware/tsp_qaoa.ipynb) | Four-city travelling salesperson problem solved with QAOA. |
| [`part01_qaoa_vqe_ibm_hardware/ibm_hardware_qaoa_guided.ipynb`](part01_qaoa_vqe_ibm_hardware/ibm_hardware_qaoa_guided.ipynb) | Guided local QAOA optimisation followed by IBM backend checks, transpilation analysis, and optional QPU submission. |
| [`part01_qaoa_vqe_ibm_hardware/monitor_ibm_job.py`](part01_qaoa_vqe_ibm_hardware/monitor_ibm_job.py) | Read-only command-line monitor for an existing IBM Runtime job. |
| [`part02_custom_penalty/custom_penalty.ipynb`](part02_custom_penalty/custom_penalty.ipynb) | Custom-penalty formulation for constrained binary optimisation. |
| [`part02_custom_penalty/example_problems.ipynb`](part02_custom_penalty/example_problems.ipynb) | Additional workshop problems. |

## Suggested teaching sequence

1. Start with the knapsack VQE or guided QAOA notebook to establish the optimisation-to-QUBO workflow.
2. Compare VQE and QAOA on the shared knapsack instance.
3. Extend the workflow to routing with the two TSP notebooks.
4. Study the custom-penalty notebook to encode constraints without slack variables.
5. Use the guided IBM hardware notebook for the real-hardware demonstration.
6. Continue with group work: formulate a problem, choose a classical or quantum approach, run experiments, analyse limitations, and prepare a final presentation.

## IBM Quantum hardware demonstration

The hardware notebook is deliberately opt-in. It first optimises the QAOA parameters locally, then separates hardware preparation from submission:

1. **Local optimisation:** run the QAOA circuit against Aer.
2. **Connect and pre-flight:** set `USE_IBM_BACKEND = True`. The notebook checks reachable operational QPUs, confirms the selected backend, reports pending jobs, and recommends the least-busy eligible backend.
3. **Before transpilation:** inspect the logical circuit, its depth, and its number of qubits.
4. **Transpile only:** set `OPTIMIZATION_LEVEL` to `0`, `1`, `2`, or `3`. Set `SHOW_ALL_OPTIMIZATION_LEVELS = True` to display all four transpiled circuits without submitting anything.
5. **Calibration/layout inspection:** compare per-qubit readout and `sx` gate errors, with the physical qubits selected by the transpiler highlighted.
6. **Submit separately:** set `SUBMIT_HARDWARE_JOB = True` only in the dedicated submission cell. The notebook submits a bounded number of shots using IBM Runtime V2 `Sampler`.
7. **Monitor and analyse:** compare raw counts, feasible-shot rate, selected feasible solution, and objective value.

### Credentials

From the repository root, copy the template only if the destination file does not already exist:

```bash
cp gate_based/part01_qaoa_vqe_ibm_hardware/.env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item gate_based\part01_qaoa_vqe_ibm_hardware\.env.example .env
```

Fill in the local `.env` file without committing or sharing it:

```text
IBM_QUANTUM_TOKEN=<your IBM Quantum API token>
IBM_QUANTUM_INSTANCE=<your IBM Quantum instance or CRN>
IBM_BACKEND=<optional operational backend name>
```

The notebook reads these values at runtime and never prints the token. The repository's `.gitignore` excludes `.env`.

### Pre-flight API note

IBM's newer `qiskit-ibm-catalog` methods are documented for the Qiskit Functions service. The hardware notebook uses IBM Runtime `QiskitRuntimeService`, so it uses the corresponding Runtime service methods instead. Runtime capacity from `service.usage()` is plan- and channel-dependent; the notebook handles an unavailable capacity report and still performs backend-access, operational-status, and least-busy checks before submission.

### Monitor an existing job

From the repository root:

```bash
python gate_based/part01_qaoa_vqe_ibm_hardware/monitor_ibm_job.py <IBM_JOB_ID> --interval 30
```

Use `--once` for a single read-only status check:

```bash
python gate_based/part01_qaoa_vqe_ibm_hardware/monitor_ibm_job.py <IBM_JOB_ID> --once
```

Runtime V2 exposes states such as `QUEUED`, `RUNNING`, `DONE`, and `CANCELLED`. Runtime V2 job objects do not generally expose an exact queue-position method, so the monitor reports queue position only when the installed API provides it.

## Safety and reproducibility notes

- Do not place IBM Quantum tokens in notebooks, source files, commits, or public issues.
- Keep `SUBMIT_HARDWARE_JOB = False` while teaching circuit construction, pre-flight checks, and transpilation.
- TSP and knapsack examples are intentionally small so that students can inspect the model, circuit, transpilation, and measurement results in one session.
- Random seeds, circuit depths, and optimiser settings are included in the notebooks to make workshop runs easier to reproduce.

See the [IBM Quantum Runtime documentation](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-runtime-primitives) for current service details.
