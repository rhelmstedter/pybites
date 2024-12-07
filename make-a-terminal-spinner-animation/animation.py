from itertools import cycle
from time import time, sleep

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
    Takes seconds argument = time for the spinner to run.
    Does not return anything, only prints to stdout."""
    infinite_spinner = cycle(SPINNER_STATES)
    end_time = time() + seconds
    while time() < end_time:
        print(next(infinite_spinner), end="\r", flush=True)
        sleep(STATE_TRANSITION_TIME)


if __name__ == "__main__":
    spinner(10)
