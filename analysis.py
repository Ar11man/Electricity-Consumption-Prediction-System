import numpy as np

def calculate_statistics(records):
    if not records:
        return None

    units = np.array([record[3] for record in records])

    total = np.sum(units)
    average = np.mean(units)
    maximum = np.max(units)
    minimum = np.min(units)

    return total, average, maximum, minimum