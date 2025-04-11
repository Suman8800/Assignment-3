import math
def main():
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    square_root = math.sqrt(number) if number >= 0 else "undefined"
    natural_log = math.log(number) if number > 0 else "undefined"
    sine_value = math.sin(number)

    print(f"Square root : {square_root}")
    print(f"logarithm: {natural_log}")
    print(f"Sine: {sine_value}")

if __name__ == "__main__":
    main()