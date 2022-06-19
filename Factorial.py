def factorial(num):
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result


def main():
    print("Welcome!")
    print("This program gives you the factorial of the number you entered.")
    inp = 0
    while inp != "exit":
        inp = input("Enter the number, or type \"exit\" to exit.\n")
        if inp == "exit":
            print("See you!")
            break
        num = 0
        try:
            num = int(inp)
            print(factorial(num))
        except Exception:
            print("You entered not a number, try again.")


if __name__ == "__main__":
    main()
