# Sigit python git exercise
# Author: Ido Noyman
# Exercise 7: Decorator Cache

def CasheDat(func, value):
    # Operating on a big function and saving the result in the "cashe" for easier and faster use next time the function is called.
    # Input: The function, The variable we want the function to work on.
    # Output: Returns the result. If the funcion has been called more than once, the result will be gathered from the cashe.

    cashe = {}

    if value in cashe:
        return cashe[value]
    else:
        result = func(value)
        cashe[value] = result # saving the result in the cashe
        return result


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    # Main example:
    
    print(CasheDat(factorial,30))
    print(CasheDat(factorial, 60))
    print(CasheDat(factorial,30))
    print(CasheDat(factorial, 60))


if __name__ == "__main__":
    main()