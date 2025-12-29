# AIDP Alpha-Ready GPU Image Inference Demo

This project is a minimal GPU compute demo designed for integration with the AIDP decentralized GPU compute network.

## What It Does
- Executes a GPU-intensive inference workload
- Demonstrates how compute jobs are abstracted for decentralized execution
- Prepares a clean interface for AIDP alpha integration

## GPU Usage
The project runs a GPU-based matrix multiplication workload using PyTorch.  
Once AIDP dApp access is available, this workload will be submitted to AIDP GPU nodes instead of local execution.

## Why AIDP
AIDP enables decentralized, low-cost, and verifiable GPU compute.  
This project aligns with AIDP’s mission by demonstrating GPU inference readiness.

## Status
AIDP dApp is currently in alpha.  
This project is built to be AIDP-compatible and ready for immediate integration once access is available.

## How to Run
```bash
pip install -r requirements.txt
python app.py