import itertools
import sys

# add return type
def batched(iterable, n):
    # do performance test
    if n < 1:
        raise ValueError("n must be at least one")
    print(f"size of csv reader: {sys.getsizeof(iterable)}")
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch