def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def main():
    sample_number = 5
    fact = factorial(sample_number)
    print(f"The factorial of {sample_number} is {fact}")
if __name__ == "__main__":
    main()
