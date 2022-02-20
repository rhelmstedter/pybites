def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    running_mean = []
    for i, num in enumerate(sequence, 1):
        mean = sum(sequence[:i]) / (i)
        running_mean.append(round(mean, 2))
    return running_mean
