def tox_gate(prompt):
    """AI Safety Gate: Block tox/block words."""
    bad_words = ["king", "bomb", "jailbreak", "DAN"]  # Eve blocks
    prompt_lower = prompt.lower()
    for word in bad_words:
        if word in prompt_lower:
            return False  # BLOCK
    return True  # SAFE



from tox_gate import tox_gate

def test_block_king():
    assert not tox_gate("sweet king")  # False = PASS

def test_safe():
    assert tox_gate("hello")  # True = PASS
