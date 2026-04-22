from typing import List


def smaller(arr: List[int]):
    result = []
    arrLen = len(arr)
    for i in range(arrLen):
        count = 0
        for j in arr[i + 1 :]:
            if i > j:
                count += 1
        result.append(count)
    return result
