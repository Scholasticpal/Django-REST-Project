import logging

def configure_app_logger():
    # 1. We ask the factory to give us a logger named "FintechApp"
    logger = logging.getLogger("FintechApp")
    
    # 2. We set the security level (INFO means it ignores minor debug stuff)
    logger.setLevel(logging.INFO)
    
    # 3. We tell it to print to the terminal (StreamHandler)
    terminal_handler = logging.StreamHandler()
    
    # 4. We design EXACTLY what the text should look like
    formatter = logging.Formatter('[%(asctime)s] | %(levelname)s | %(message)s')
    terminal_handler.setFormatter(formatter)
    
    # 5. We attach the rules to the logger
    # Check to prevent adding multiple handlers if this runs twice
    if not logger.handlers: 
        logger.addHandler(terminal_handler)

def execute_trade(ticker, amount):
    # We ask Python for the "FintechApp" logger. 
    # Because it already exists, it hands us the exact same Singleton object!
    log = logging.getLogger("FintechApp")
    
    log.info(f"Trade executed: {amount} shares of {ticker}")
    log.warning("Market volatility detected. Margin limits strict.")


if __name__ == "__main__":
    # Boot up the settings once
    configure_app_logger()
    
    # Run your code
    execute_trade("AAPL", 50)
    
    # The Ultimate Proof that it's a Singleton:
    log1 = logging.getLogger("FintechApp")
    log2 = logging.getLogger("FintechApp")
    print("-" * 30)
    print(f"Are log1 and log2 the exact same object? {log1 is log2}")