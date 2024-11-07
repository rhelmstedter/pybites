def fizzbuzz(num):
    if num % 15 == 0:
        return "Fizz Buzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    return num


if __name__ == "__main__":
    print(fizzbuzz(0))
