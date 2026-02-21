# nodezerov2

[![Tests](https://github.com/lukeagi/nodezerov2/actions/workflows/drift.yml/badge.svg)](https://github.com/lukeagi/nodezerov2/actions/workflows/drift.yml)
[![PyPI](https://badge.fury.io/py/nodezerov2.svg)](https://pypi.org/project/nodezerov2/)
[![Docker]![NodeZeroV2](https://img.shields.io/badge/NodeZeroV2-AI%20Safety%20Gates-brightgreen?logo=python&logoColor=white)[file:139]


# NodeZeroV2 🛡️ AI Safety Gates

Tox/drift blocks vs. Dany exploits + jailbreaks. MIT open.

## Quick Deploy
```bash
# Pip
pip install nodezerov2
pytest

# Docker
docker pull lukeagi/nodezerov2:latest
docker run pytest



drift_detector → tox_gate('sweet king') → BLOCKED → glass_box_log
