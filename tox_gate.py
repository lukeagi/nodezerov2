def tox_gate(prompt):
    """AI Safety Gate: Block tox/block words."""
    bad_words = ["king", "bomb", "jailbreak", "DAN"]  # Eve blocks
    prompt_lower = prompt.lower()
    for word in bad_words:
        if word in prompt_lower:
            return False  # BLOCK
    return True  # SAFE
