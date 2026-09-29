# Problem 3: Accumulator Function with Scope
# [Create a function create_bank_account(initial_balance)]:

# 1. Define an inner function transaction(amount, type="deposit").

# 2. Use the nonlocal keyword to update and track initial_balance across multiple transactions.

# 3. Ensure the account cannot be overdrawn (if type == "withdraw" and amount > balance, raise an error or print a warning).

def create_bank_account(initial_balance):
    balance = initial_balance

    def transaction(amount, type="deposit"):
        nonlocal balance

        if type == "deposit":
            balance += amount
        elif type == "withdraw":
            if amount > balance:
                raise ValueError("Not enough balance")
            balance -= amount
        else:
            raise ValueError("Invalid transaction type")

        return balance

    return transaction


account = create_bank_account(1000)
print(account(200))   # deposit
print(account(50, "withdraw"))    # withdraw        
