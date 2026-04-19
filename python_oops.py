class Trader:
    total_traders = 0
    
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        Trader.total_traders += 1
    
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    
    def __add__(self, other):
        new_name = self.name + "&" + other.name
        new_balance = self._balance + other._balance
        return Trader(new_name, new_balance)



class PremiumTrader(Trader):
    def __init__(self, name, balance, margin_limit):
                
        super().__init__(name, balance)
        self.margin_limit = margin_limit

    def deposit(self, amount):
        amount += amount*0.10
        self._balance += amount
        return self._balance



class CryptoBot:
    def __init__(self, balance):
        self.crypto_balance = balance
    
    def get_balance(self):
        return self.crypto_balance


def audit_account(entity):
    print(f"Auditing account. current funds: {entity.get_balance()}")








if __name__ == "__main__":
    t1 = Trader("Alice", 1000)
    t2 = Trader("Arjun", 3000)
    t1.deposit(500)
    print(t1.get_balance())
    
    pt = PremiumTrader("Bob", 1000, 5000)
    pt.deposit(100)
    print(f"Premium balance: {pt.get_balance()}")
    
    
    print(Trader.total_traders)
    merged_account = t1+t2
    print(merged_account.name)
    print(merged_account.get_balance())
    print(Trader.total_traders)
    
    bot= CryptoBot(8000)
    
    audit_account(pt)
    audit_account(bot)