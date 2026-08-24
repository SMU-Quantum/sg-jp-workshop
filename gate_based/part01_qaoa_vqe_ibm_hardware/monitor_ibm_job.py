"""Monitor an IBM Quantum Runtime job without submitting a new job."""

import argparse
import os
import time
from datetime import datetime
from pathlib import Path

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService


FINAL_STATES = {"DONE", "CANCELLED", "ERROR"}


def repository_root() -> Path:
    for path in (Path.cwd(), *Path.cwd().parents):
        if (path / ".env.example").exists():
            return path
    return Path.cwd()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job_id", help="IBM Quantum Runtime job ID")
    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Seconds between status checks (default: 30)",
    )
    parser.add_argument(
        "--once",
        action="store_true",
        help="Print one status update and exit",
    )
    args = parser.parse_args()

    load_dotenv(repository_root() / ".env")
    token = os.getenv("IBM_QUANTUM_TOKEN")
    instance = os.getenv("IBM_QUANTUM_INSTANCE")
    if not token:
        raise RuntimeError("IBM_QUANTUM_TOKEN is not set in .env")

    service = QiskitRuntimeService(
        channel="ibm_quantum_platform",
        token=token,
        instance=instance or None,
    )
    job = service.job(args.job_id)

    while True:
        status = str(job.status())
        queue_position = "unavailable from RuntimeJobV2"
        if hasattr(job, "queue_position"):
            try:
                queue_position = job.queue_position(refresh=True)
            except Exception:
                queue_position = "unavailable"

        timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
        print(f"{timestamp} | job={args.job_id} | status={status} | queue position={queue_position}")

        if args.once or status in FINAL_STATES:
            break
        time.sleep(max(args.interval, 1))


if __name__ == "__main__":
    main()
