def sum_numeric(limit = 10) -> int:
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s

wyniki = []
wyniki.append(sum_numeric(20))
wyniki.append(sum_numeric(21))
wyniki.append(sum_numeric(22))
wyniki.sort()
print(wyniki)