def get_xp_for_action(action):
    rules = {
        "chat": 5,
        "resume": 20,
        "project": 15
    }
    return rules.get(action, 0)
