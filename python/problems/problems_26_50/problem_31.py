def coin_sum_combos(balance):
    '''
    return the number of ways that balance can be 
    built using various british coins (pence + pounds)

    Possible coins to use are
    1p, 2p, 5p, 10p, 20p, 50p, 1P, and 2P 
    '''
    starting_balance = balance
    combos = 0
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    for coin in coins:
        while coin <= balance:
            balance -= coin
            if balance != 0:
                combos += coin_sum_combos(balance)
        if balance == 0:
            combos += 1
            balance = starting_balance
    
    return combos



print coin_sum_combos(200)

    
