def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA strands has to be of equal length.")
    count = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            count += 1
    return count


# different and shorter solution:
def _distance(strand_a, strand_b):
    return sum(a != b for a, b in zip(strand_a, strand_b))

