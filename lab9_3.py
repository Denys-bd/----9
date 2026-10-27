metals = {}

for i in range(9):
    name = input(f"Введіть назву металу {i + 1}: ")
    density = float(input(f"Введіть густину металу {name} (г/см³): "))
    metals[name] = density

# Сортування за алфавітом
alphabetical = dict(sorted(metals.items()))

print("\nМетали за алфавітом:")
for name, density in alphabetical.items():
    print(f"{name}: {density} г/см³")

# Сортування за густиною у порядку зменшення
by_density = sorted(
    metals.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nМетали за густиною (від більшої до меншої):")
for name, density in by_density:
    print(f"{name}: {density} г/см³")

# Виведення металу посередині списку
middle = by_density[len(by_density) // 2]

print("\nМетал посередині списку за густиною:")
print(f"Назва: {middle[0]}")
print(f"Густина: {middle[1]} г/см³")