## Architecture Overview

This project is designed as an alpha-ready GPU compute demo compatible with AIDP’s decentralized GPU network.

### Compute Flow
1. The application submits a GPU workload request.
2. The GPU job is abstracted to be executed by an external compute provider.
3. Once AIDP dApp access is live, this job will be routed to AIDP decentralized GPU nodes.
4. The result is returned to the application layer.

### Why AIDP
AIDP provides decentralized, verifiable GPU compute suitable for AI inference, rendering, and HPC workloads. This project demonstrates a minimal GPU inference workload aligned with AIDP’s compute model.
