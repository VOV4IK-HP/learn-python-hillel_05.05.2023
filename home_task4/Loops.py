EXIT_COMMAND = 'sum'
while True:
    x = input('Are you studying or working (type `sum` to leave)? ')
    if 'sum' == x.lower():
        print('About to exit')
        exit()
        print('Already exited')
    else:
        print('Вы не вышли')

print('Outside exit-while!')