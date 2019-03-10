#Sigit python git exercise
#author: Ido Noyman
#Exercise 1: ATM simulation.


def check_secret_code(user):
    #Checks the user's secret code
    #input: dictionary with the user attributes.
    #output: returns true if the input code matches the user's code, else returns false after 5 failed attempts.

    print("Enter your secret code:")
    secretCode = input()
    atmpts = 4
    while secretCode != user["secretcode"] and atmpts > 0:
        print("Incorrect! try again:")
        atmpts -= 1
        secretCode = input()
    return secretCode == user["secretcode"]



def print_user_balance(user):
    # Print the balance in the user account.
    # input: dictionary with the user attributes.
   
    print("Balance:", user["balance"])

def get_money(user):
    # Withdraw money from the user's account.
    # input: dictionary with the user attributes.

    print("Enter how much money to withdraw:")
    user["balance"] -= int(input())


def change_secret_code(user):
    # Changes the user's secret code, to in-function input.
    # input: dictionary with the user attributes.

    print("Enter new secret code (4 digits):")
    user["secretcode"] = input()


def main():

    functions = {"1": print_user_balance, "2": get_money, "3": change_secret_code}
    user = {"secretcode": "5273", "balance": 67200}

    if not check_secret_code(user):
        print("Too many failed attempts, your are blocked.")
        return

    print("Choose an action: \n" +
          "1 = print your balance. \n" +
          "2 = withdraw money. \n" +
          "3 = change code. \n" +
		  "press any other key to exit.")

    p = input()
    while p in functions.keys():
        functions[p](user)
        # print(user) # DEBUG print
        if not check_secret_code(user):
            print("Too many failed attempts, your are blocked.")
            return
			
        print("Choose another action: \n" +
          "1 = print your balance. \n" +
          "2 = withdraw money. \n" +
          "3 = change code. \n" +
		  "press any other key to exit.")
        p = input()


if __name__ == '__main__':
    main()