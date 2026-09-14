product = {
    'food':1500,
    'apple':50,
    'mobile':2000,
    'labtob':5000,
}

balance = 0

while True:
    choice = input('''choose;
    [0] foode 1500
    [1] apple 50
    [2] mobile 2000
    [3] labtop 5000
    [4] select all 
    [5] buy 
    >>> ''')
    if choice == '0':
        balance += 1500
        print(balance)
    elif choice == '1':
        balance += 50
        print(balance)
    elif choice == '2':
        balance += 2000
        print(balance)
    elif choice == '3':
        balance += 5000
        print(balance)
    elif choice == '4':
        balance += 8550
        print(balance)
    elif choice == '5':
        value = float(input('value:'))
        if value > 5000 :
            value_d = value - (value * (20/100))
            balance -= value_d
            print('you have discount')
            print(f'bedehi : {balance}')
        else:
            balance -= value
            print(f'bedehi : {balance}')