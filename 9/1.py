def multiplication(n1, n2):
    result = 0
    if n1 < 0 and n2 < 0:
        return multiplication(-n1, -n2)
    for _ in range(abs(n2)):
        result += n1
    return result

print(multiplication(-2, 6))

assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0