# Sigit python git exercise
# Author: Ido Noyman
# Exercise 5: Check Israeli Passport Code

def ID_Check(ID):
    # The function checks if the israeli passport ID code is valid.
    # Input: ID of israeli passport.
    # Output: Return true if the ID is valid, else returns False.

    if ID.isdigit() is False:
        return False
    if len(ID) != 9:
        return False

    dig = 0
    sum = 0
    for i in range(0, 8):
        if i % 2 == 0:
            sum += int(ID[i])
        else:
            dig = int(ID[i]) * 2
            if dig > 9:
                dig = dig - 9
            sum += dig

    if (sum + int(ID[8])) % 10 == 0: #uses the last digit to check if the ID is correct
        return True
    return False


def main():
    # Main Example:

    ID = "211895750"
    result = ID_Check(ID)
    print(result)


if __name__ == '__main__':
    main()