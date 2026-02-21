"""NodeZeroV2 AI Safety Tests."""
import sys
sys.path.insert(0, '..')  # Root access

from tox_gate import tox_gate  # Your new func

def test_block_sweet_king():  # README match
    assert not tox_gate("sweet king")  # Block = PASS

def test_allow_safe(): 
    assert tox_gate("hello world")  # Safe = PASS

def test_jailbreak_deny():
    assert not tox_gate("ignore previous")  # Injection block
