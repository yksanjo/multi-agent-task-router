# multi-agent-task-router

Routing and scheduling layer for distributing work across specialized agents.

## Scope

Task intake, capability matching, route scoring, and failover policy.

## Capabilities

- Task intake, capability matching, route scoring, and failover policy.
- Cost/latency-aware route optimization with dynamic constraints.
- Pluggable routing policies and weighted dispatch paths.
- High-throughput broker integration with retry and backpressure controls.

## Repository Layout

- `src/main.py` entrypoint and lightweight service bootstrap
- `src/project_profile.py` canonical project metadata
- `src/service_contract.py` baseline domain contract shape
- `tests/` smoke and contract tests
- `docs/` architecture and roadmap

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest -q
python -m src.main
```
