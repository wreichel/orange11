#
#
# while designs:
#     current_designs = designs.pop()
#     print(f"Wydruk modelu: {current_designs}")
#     models.append(current_designs)
#
#     print("Wydrukowane zostały modele:")
#     for model in models:
#         print(model)


def print_models(unprinting, completed):
    while unprinting:
        current_designs = unprinting.pop()
        print(f"Wydruk modelu: {current_designs}")
        completed.append(current_designs)

def show_completed(completed):
    print("Wydrukowane zostały modele:")
    for model in completed:
        print(model)