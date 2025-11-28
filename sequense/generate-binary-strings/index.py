def solve(ind, flag, numbers, result):
    if ind >= len(numbers):
        result.append("".join(numbers))
        return
    numbers[ind] = "0"
    solve(ind + 1, True, numbers, result)
    if flag:
        numbers[ind] = "1"
        solve(ind + 1, False, numbers, result)
        numbers[ind] = "0"


def genebstrings(n):
    numbers = ["0"] * n
    result = []
    solve(0, True, numbers, result)
    return result


result = genebstrings(3)
print(result)
