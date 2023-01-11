def example(a, b, **kwargs):
    return a * b - kwargs


# print(type(example))
# print(example.__code__.co_varnames)
# print(example.__code__.co_argcount)

liczymy = lambda x, y: y * x - 1

# print(liczymy(100, 99))

r_0 = {'miasto': 'Kielce'}
r_1 = {'miasto': 'Kielce', 'ZIP': '25-900'}

d_zip = lambda row: row.setdefault('ZIP', '00-000')

# print(d_zip(r_0))
# print(r_0)
# print(d_zip(r_1))
# print(r_1)

lata = [(2000, 29.81), (2001, 8.32), (2002, 12.234), (2003, 45.765), (2005, 334.3), (2006, 23.43), (2008, 45.1)]

# print(max(lata))
# print(max(map(lambda c: (c[1], c), lata))[1])

# print(min(lata))

print(0 and 'right')
print(True and 'right')