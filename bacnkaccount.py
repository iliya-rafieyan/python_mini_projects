balance = 0
while True:
    Password = input('enter pass :')
    if Password == '1234':
        choice = input('''select:
        [0] variz
        [1] baradasht
        [2] namayesh hesab banki
        >>>
        ''')

        if choice == '0':
            value = float(input('value : '))
            balance += value
            print('variz shod !!!')
        elif choice == '1':
            value2 = float(input('value : '))
            balance -= value2
            print('baradasht show')
        elif choice == '2':
            print('account: ' , balance)
        else:
            print('ERROR !')