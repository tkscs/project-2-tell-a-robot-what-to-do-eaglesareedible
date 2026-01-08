state = 'locked'
while True:
    while state =='locked':
        state = input('Select either pay, or leave\n')
        if state=='pay':
            depositedamount = input("How much do you want to enter? Menu is \n $1.5 for sprite and cola \n $2 for chips. \n")
            balance = float(depositedamount)
            state = 'unlocked'
        elif state =='leave':
            False
    while state=='unlocked':
        state = input('Do you want to leave, or what do you want to buy?\n$1.50 Cola? Sprite?\n$2.00 Chips? ')
        if state=='Cola':
            if balance<1.5:
                balance=balance-balance
                print("INSUFFICIENT FUNDS, CURRENT BALANCE DISPENSED, RETURN TO START")
                state = 'locked'
            elif balance>=1.5:
                print('Cola has been dispensed, dispensing change \nPlease enjoy!')
                balance = balance-1.50
                state = 'locked'
        elif state =='Sprite':
            if balance<1.5:
                balance=balance-balance
                print("INSUFFICIENT FUNDS, CURRENT BALANCE DISPENSED, RETURN TO START")
                state = 'locked'
            elif balance>=1.5:
                print('Sprite has been dispensed, dispensing change \nPlease enjoy!')
                balance = balance-1.50
                state = 'locked'
        elif state =='Chips':
            if balance<2:
                balance=balance-balance
                print("INSUFFICIENT FUNDS, CURRENT BALANCE DISPENSED, RETURN TO START")
                state = 'locked'
            elif balance>=2:
                print("Chips have been dispensed, dispensing change. \nPlease enjoy!")
                balance = balance-2.00
                state = 'locked'
    if state == 'leave':
        False
