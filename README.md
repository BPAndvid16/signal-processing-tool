# BioSignal Processing Tool (Educational)

A modular educational tool for loading biological signals (CSV and MAT/HEA),
selecting a signal type (ECG/EEG/EMG/PPG/Temperature/Respiration), and applying
an appropriate processing pipeline with clear, human-readable rationale.

## Goals
- Unified data ingestion (CSV + MAT/HEA)
- Signal-type specific processing pipelines
- Transparent reporting: what was applied and why
- Reproducible runs (CLI + saved outputs)

## Project Structure
- `src/` core library
- `src/io/` loaders (CSV, MAT/HEA)
- `src/pipelines/` processing pipelines by signal type
- `src/report/` figures and report generation
- `scripts/` command-line entrypoints
- `outputs/` generated results (ignored by git)

## Disclaimer
This tool is for educational purposes only and is not intended for clinical diagnosis.# signal-processing-tool
