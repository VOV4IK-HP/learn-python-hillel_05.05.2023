x = [3, 4, 5, 6]
print(len(x))

x = [5, 7, 4]
print(type(x))

x = [5, 7, 4]
x[2] = 5
print(x)

x = (2, 3, 8)
print(type(x))

'''x = (2, 3, 8)
x[2] = 7
print(x)'''

x = [2, 3, 4]
for element in x:
    element += 3
print(x)

x = [2, 3, 4]
new_x = list()
for element in x:
    new_x.append(element + 3)
print(new_x)

x = [8, 5, 22]
print(sorted(x))

x = [4, 5, 6]
new_x = list()
i = 0
for element in x:
    new_x.append(x[i] + 3)
    i += 1
print(new_x)

x = [1, 5, 8, 9, 10]
print(x[:2])

x = (1, 5, 8, 9, 10)
print(x[3:])

x = [1, 5, 8, 9, 10]
print(x[-2:])

x = [1, 5, 8, 9, 10]
print(x[:100])

x = [1, 5, 8, 9, 10]
print(x[-100:])

x = [1, 5, 8, 9, 10]
print(x[::2])

x = [1, 5, 8, 9, 10]
print(x[::-1])

x = {1, 5, 8, 9, 10}
x.add(6)
print(7 in x)