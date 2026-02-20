import pytest
from nodezero_v2 import nodezero_v2_gate  # Adjust import path

def test_daenerys_block():
    assert not nodezero_v2_gate('sweet king')[0]

def test_safe_pass():
    assert nodezero_v2_gate('hello world')[0]

def test_drift_detector():
    priors = ["safe prior"]
    assert drift_detector(priors, 'sweet king')  # True = block
