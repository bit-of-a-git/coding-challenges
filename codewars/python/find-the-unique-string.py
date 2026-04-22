from collections import Counter


def find_uniq(arr):
    counter = Counter()
    for item in arr:
        chars = "".join(sorted(set(item.lower().strip())))
        counter[chars] += 1

    for item in arr:
        chars = "".join(sorted(set(item.lower().strip())))
        if counter[chars] == 1:
            return item
