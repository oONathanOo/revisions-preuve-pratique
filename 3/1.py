def fibonacci(n):
    result = [1,1]
    if n in [1, 2]:
        return 1
    for i in range(n-2):
        result.append(result[i]+result[i+1])
    return result[-1]


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025