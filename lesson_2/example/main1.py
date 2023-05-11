from math import sqrt
a = float(input("Type your first number here ->> "))
b = float(input("Type your second number here ->> "))
c = float(input("Type your third number here ->> "))

d = b ** 2 - 4 * a * c
print(d)

if d >= 0:
    print("Yes, it`s bigger")
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(x1)
    print(x2)
else:
    print("Not, it`s not")