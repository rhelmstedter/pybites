MIN_DRIVING_AGE = 18


def allowed_driving(name: str, age: int) -> None:
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age < 18:
        print(f'{name} is not allowed to drive')
    else:
        print(f'{name} is allowed to drive')