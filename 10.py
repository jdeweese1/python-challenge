# Problem 10
# a = [1, 11, 21, 1211, 111221, ]
# len(a[30] = ?

# https://oeis.org/A005150 look and say sequence


def f(n):
    p = "1"
    seq = [1]
    while n > 1:
        q = ''
        idx = 0  # Index
        length = len(p)  # Length
        while idx < length:
            start = idx
            idx = idx + 1
            while idx < length and p[idx] == p[start]:
                idx = idx + 1
            q = q + str(idx - start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq


answer = f(31)[30]
print(f'a[30] is {answer} \nlen(a[30] is {len(str(answer))}')
# 5808
