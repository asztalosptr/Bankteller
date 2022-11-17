checking_balance = 0
savings_balance = 0

def check_balance(account_type, checking_balance,  savings_balance):
    if account_type == 'savings':
        balance = savings_balance
    elif account_type == 'checking':
        balance = checking_balance
    else:
        return 'Unsuccessful, please enter \'checking\' or \'savings\''
    
    balance_statement = f'Your {account_type} balance is {balance}'
    return balance_statement
     
     
print(check_balance('checking', checking_balance, savings_balance))
print(check_balance('savings', checking_balance, savings_balance))

def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status = ''
    if amount > 0:
        if account_type == 'savings':
            savings_balance += amount
            deposit_status = 'successful'
        elif account_type == 'checking':
            checking_balance += amount
            deposit_status = 'successful'
        else:
            deposit_status = 'Unsuccessful, please enter \'checking\' or \'saving\''
    else:
        return "Unsuccessful, please enter an amount greater than 0"
    
    deposit_statement = f'Deposit of {amount} to your {account_type} account was {deposit_status}.'
    print(deposit_statement)
    
    return checking_balance, savings_balance
    
    
checking_balance, savings_balance =  make_deposit('savings', 10, checking_balance, savings_balance)
print(check_balance('savings', check_balance, savings_balance))

checking_balance, savings_balance =  make_deposit('checking', 200, checking_balance, savings_balance)
print(check_balance('checking', checking_balance, savings_balance))


def make_withdrawal(account_type, amount, checking_balance, savings_balance):
    withdrawal_status = ''
    fail = 'Unsuccessful, please enter amount less than balance'
    if account_type == 'savings':
        if amount > savings_balance:
            withdrawal_status = fail
        else:
            savings_balance -= amount
            withdrawal_status = 'successful'
    elif account_type == 'checking':
        if amount > checking_balance:
            withdrawal_status = fail
        else:
            checking_balance -= amount
            withdrawal_status = 'successful'
    else:
        withdrawal_status = 'Unsuccessful, please enter \'checking\' or \'saving\''
        
    withdrawal_statement = f'Withdrawal of {amount} from your {account_type} account was {withdrawal_status}.'
    print(withdrawal_statement)
    return checking_balance, savings_balance

checking_balance, savings_balance = make_withdrawal('savings', 11, checking_balance, savings_balance)
print(check_balance('savings', checking_balance, savings_balance))

checking_balance, savings_balance = make_withdrawal('checking', 170, checking_balance, savings_balance)
print(check_balance('checking', checking_balance, savings_balance))


def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    transaction_status = ''
    trans_error = 'Unsuccessful, please enter amount less than '
    
    if acc_from == 'savings' and acc_to == 'checking':
        if amount > savings_balance:
            transaction_status = trans_error + str(savings_balance)
        else:
            savings_balance -= amount
            checking_balance += amount
            transaction_status = 'successful'
            
    elif acc_from == 'checking' and acc_to == 'savings':
        if amount > checking_balance:
            transaction_status = trans_error + str(checking_balance)
        else:
            checking_balance -= amount
            savings_balance += amount
            transaction_status = 'successful'
    else:
        transaction_status = 'Unsuccessful, please enter \'checking\' or \'saving\''    
        
    transaction_statement = f'Transfer of {amount} from your {acc_from} to your {acc_to} account was {transaction_status}.'
    print(transaction_statement)
    return checking_balance, savings_balance

checking_balance, savings_balance = acc_transfer('checking', 'savings', 10, checking_balance, savings_balance)
print(check_balance('checking', checking_balance, savings_balance))

checking_balance, savings_balance = acc_transfer('savings', 'checking', 5, checking_balance, savings_balance)
print(check_balance('savings', checking_balance, savings_balance))

print(check_balance('checking', checking_balance, savings_balance))
print(check_balance('savings', checking_balance, savings_balance))




        
        
