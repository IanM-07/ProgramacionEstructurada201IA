def factorial():
    n = int(input("Ingrese un numero: "))
    print(n)
    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i
        i = i + 1
    return factorial

def main():
    factorial_n = factorial()
    print(factorial_n)

if __name__ == "__main__":
    main()
    