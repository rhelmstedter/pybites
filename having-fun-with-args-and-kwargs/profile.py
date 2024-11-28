def get_profile(name, age, *sports, **awards) -> dict:
    if not isinstance(age, int):
        raise ValueError
    profile = {"name": name, "age": age}
    if sports:
        if len(sports) > 5:
            raise ValueError
        profile["sports"] = sorted(sports)
    if awards:
        profile["awards"] = awards
    return profile
