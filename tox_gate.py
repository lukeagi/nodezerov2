def tox_gate(prompt):
    bad = ['king', 'jailbreak', 'exploit', 'bomb']
    return not any(word in prompt.lower() for word in bad)
