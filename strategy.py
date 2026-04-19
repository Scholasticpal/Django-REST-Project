def standard_fee_strategy(amount):
    return amount * 2

def premium_fee_strategy(amount):
    return amount * 5


class TradeTransaction:
    # We pass the strategy function directly into the object!
    def __init__(self, amount, fee_strategy):
        self.amount = amount
        self.fee_strategy = fee_strategy
        
    def func(self):
        fee = self.fee_strategy(self.amount)
        print(f"Total fee: {fee}")

standard_trade = TradeTransaction(1000, standard_fee_strategy)
premium_trade = TradeTransaction(1000, premium_fee_strategy)

standard_trade.func()
premium_trade.func()

# strategy - wanna use a class that can take out desired function as argument. this way we can separate out behaviour of our object based on the function we pass without needing to call if else again n again.