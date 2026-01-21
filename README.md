# gv-sanity-check
Detects stability drift between metric snapshots in CI pipelines.

# GV Sanity Check

A lightweight GitHub Action that flags stability drift between metric snapshots.

## Usage

```yaml
- uses: willshacklett/gv-sanity-check@v1
  with:
    metrics_file: metrics.json
    baseline_file: baseline.json
