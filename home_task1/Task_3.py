# Розрахунок витрати палива автомобіля

a = float(input("Введіть витрату палива за 100км., л. ->> "))
b = float(input("Введіть вартість плива за 1л., грн. ->> "))
c = float(input("Введіть відстань яку треба здолати, км. ->> "))

# сумарна витрата палива, л.:
d = a / 100 * c
print('сумарна витрата палива, л.:')
print(float(d))

# сума витрат, грн.:
e = d / 100 * c * b
print('сума витрат, грн.:')
print(float(e))