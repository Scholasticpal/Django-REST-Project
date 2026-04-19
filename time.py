import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Total time taken to execute: ",end_time-start_time)
        
    return wrapper

@timer
def heavy_computation(val):
    for i in range(0,val):
        print(f"Computation no. {i}")

if __name__ == "__main__":
    heavy_computation(11)