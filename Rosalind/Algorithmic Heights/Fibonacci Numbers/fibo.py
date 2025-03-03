def fibonacci_number(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n > 1: return fibonacci_number(n - 1) + fibonacci_number(n - 2)

if __name__ == "__main__":
    with open("rosalind_fibo.txt", "r") as f:
        n = int(f.readline().strip())
        print(fibonacci_number(n))