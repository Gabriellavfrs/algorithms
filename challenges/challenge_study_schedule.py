def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None
    for login, logout in permanence_period:
        if type(login) != int or type(logout) != int:
            return None
        if login <= target_time and logout >= target_time:
            counter += 1
    return counter
