# Sigit python git exercise
# Author: Ido Noyman
# Exercise 6: Creating Map

def newMap(Fun, List):
    # Creating the map function. Running a function on all items is a list/
    # input: a Function and a list
    # output: Every item in the list will be changed according to the function (Fun), and then this function will return a list with all the changed items.

    newList = []
    for item in List:
        newList.append(Fun(item))
    return newList

def power(num):
    return int(num) * int(num)

def main():
	# Main example:

    numbers = ["52", "44", "532"]
    newList = newMap(power, numbers)
    for item in newList:
        print(item)

if __name__ == '__main__':
    main()