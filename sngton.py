# q1. singleton design pattern states that if there exists an object of a class, and we try to call method of that class by creating identical object again, then we should reuse the original object. In prod systems this is to avoid the recreation of objects at every client req. like say in db calls. to implement this, we make use of a special dunder method called __new__ it basically is responsible for allocating memory to an object during its creation. so if we already have one existing, we can check that using a function and return the same, else we can call the __new__ class user super() method.

# q2. __new__ allocates memory to an class object before its instanciation. __init__ runs when we create a class object, to declare instance variables for that object.
#q3.
class SingletonLogger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("creating new logger")
            cls._instance  = super().__new__(cls)
        else:
            print("returning existing logger")
        return cls._instance
    
    def log(self, msg):
        print(f"[log]: {msg}")
    

if __name__ == "__main__":
    # Test to prove they are the same object
    log1 = SingletonLogger()
    log2 = SingletonLogger()
    
    print(log1 is log2)