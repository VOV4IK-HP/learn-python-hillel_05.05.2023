# Розрахунок податку від надходження на рахунок підприємця

a = float(input("Введіть розмір надходження, грн. ->> "))
b = float(input("Введіть відсоток податка, % ->> "))

# сума податку, грн.:
c = a / 100 * b
print('сума податку, грн.:')
print(float(c))

# сума прибутку за вирахуванням податку, грн.:
d = a - (a / 100 * b)
print('сума прибутку за вирахуванням податку, грн.:')
print(float(d))