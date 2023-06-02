# Расчет показаний счетчика:
old_data = float(input("Введите предыдущие показания счетчика, кВт\n ->> "))
new_data = float(input("Введите текущие показания счетчика, кВт\n ->> "))
price = float(input("Введите тариф, грн/кВт\n ->> "))

# Использовано кВт, грн.:
used = new_data - old_data

# Нужно оплатить, грн.:
coast = used * price

print('Использовано, кВт.:')
print(float(used))
print('Нужно оплатить, грн.:')
print(float(coast))