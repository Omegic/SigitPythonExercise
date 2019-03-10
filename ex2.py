#Sigit python git exercise
#author: Ido Noyman
#Exercise 2: Summation of a list


def MakeList():
    # Part A: Creating the list with the user's input

    list = []
    n = input("Enter a number to enter to the list : ")
    while n != 'stop':
        if n.isdigit():
            list.append(int(n))
        else:
            print("Invalid number")
        n = input("Enter a number to enter to the list : ")
    summary = SumList(list)
    print("The sum of the list is: " + str(summary))
    return


def SumList(sumList):
    # Part B: Calculatin the sum of the list

    sum = 0
    for i in sumList:
        sum += i
    return sum


def main():
    MakeList()


if __name__ == '__main__':
    main()