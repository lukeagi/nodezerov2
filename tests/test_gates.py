import pytest
from nodezero_v2.gate import tox_gate  # Assumes gate.py exists
from nodezero_v2 import drift_detector  # Main import

def test_daenerys_block():
    """Sweet king → BLOCKED (Daenerys gate)."""
    assert not tox_gate("sweet king")  # Fails tox

def test_safe_pass():
    """Hello world → SAFE."""
    assert tox_gate("hello world")

def test_drift_detector():
    """Prior responses → safe."""
    priors = ["safe prior 1", "safe prior 2"]
    safe, daenerys = drift_detector(priors)
    assert safe  # No drift triggers

# Run all
pytest.main(["-v"])
