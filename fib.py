# fibonacci.py

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
    fib_sequence = fibonacci(num_terms)
    print("Fibonacci Sequence:")
    print(fib_sequence)

if __name__ == "__main__":
    main()
