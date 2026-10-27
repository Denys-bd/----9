K = {n for n in range(-34, 45) if abs(n) % 10 == 4}

print("Початкова множина K:", sorted(K))

K = {n for n in K if n % 4 != 0}

print("Множина K після видалення чисел, які діляться на 4:", sorted(K))