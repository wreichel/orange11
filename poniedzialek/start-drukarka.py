from pakiet import drukarka

designs = ['telefon', 'robot', 'sześcian']
models = []

print("coś wykonujemy...")
drukarka.print_models(designs, models)
drukarka.show_completed(models)

input("Aby zakończyć wciśnij ENTER")

# global_adj: float
# global_adj = 3.6


def some_fun(a: float, b: float, t: float) -> float:
    return a + b * t
    _
    global_adj

print(some_fun(4, 3, 2))