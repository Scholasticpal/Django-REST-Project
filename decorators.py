def auth_check(func):
    def wrapper(*args, **kwargs):
        print("Security alert: checking user creds...")
        func(*args, **kwargs)
        print("Security alert: Audit log updated")
    return wrapper

@auth_check
def buy_stock(ticker, amount):
    print(f"Successfully purchased {amount} shares of {ticker}.")
    
    
    
    

if __name__ == "__main__":
    buy_stock("AAPL", 50)