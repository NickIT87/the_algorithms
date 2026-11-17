from concurrent.futures import ProcessPoolExecutor
import os

def calculate(x):
    return x ** 2

if __name__ == "__main__":
    print(os.cpu_count())
    
    with ProcessPoolExecutor(
        max_workers=os.cpu_count()
    ) as executor:
        results = list(
            executor.map(calculate, range(100))
        )

    print(results)