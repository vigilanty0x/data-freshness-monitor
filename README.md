# Data Freshness Monitor

Deterministic dataset freshness decisions with unknown timestamps blocked.

Public offline Python MVP using only the standard library. Inputs are bounded, failures remain visible, and all examples/tests use synthetic data.

## CLI

```bash
python -m data_freshness_monitor.cli input.json
python -m unittest discover -s tests -v
python scripts/check.py
```

The public Python API is `data_freshness_monitor.core.run(data)`. The CLI accepts the same JSON object from a path or standard input and emits machine-readable JSON.

Apache License 2.0.

