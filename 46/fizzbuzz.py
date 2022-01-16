def fizzbuzz(num):
    if not num % 15:
        return "Fizz Buzz"
    elif not num % 5:
        return "Buzz"
    elif not num % 3:
        return "Fizz"
    return num
