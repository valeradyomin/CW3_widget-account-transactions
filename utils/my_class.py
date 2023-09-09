class Transaction:
    def __init__(self, id, state, date, amount, currency, description, from_account, to_account):
        self.id = id
        self.state = state
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_account = from_account
        self.to_account = to_account

    def __repr__(self):
        return (f"Transaction"
                f"(id={self.id}, state={self.state}, date={self.date}, amount={self.amount},"
                f" currency={self.currency}, description={self.description},"
                f" from_account={self.from_account}, to_account={self.to_account})")
