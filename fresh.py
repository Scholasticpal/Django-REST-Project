def log_trade(trade_id, *args, **kwargs):
    
    print(f"Main Trade ID: {trade_id}")
    print(f"Additional Info (Args): {args}")
    print(f"Detailed metadata (Kwargs): {kwargs}")
    
    print("-" * 30)
    
if __name__ == "__main__":
    log_trade("TXN-100")
    log_trade("TXN-101", "BUY", "NIFTY50", 25000)
    
    log_trade("TXN-102", ["BUY", "SELL", "SGB"], user="Alice", ip_address = "192.168.1.1", status="success")