class DBConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Building a brand new connection")
            
            cls._instance = super().__new__(cls)
        else:
            print("Reusing existing DB Connection")
        
        return cls._instance

if __name__ == "__main__":
    print("User 1...")
    user1_db = DBConnection()
    
    print("User2....")
    user2_db = DBConnection()
    
    print("User3...")
    user3_db = DBConnection()
    
    print("-"*30)
    