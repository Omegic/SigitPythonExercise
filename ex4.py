#Sigit python git exercise
#author: Ido Noyman
#Exercise 4: Compressing a string

def CompressString(st):
    # Compress a given string into a shorter string by implying the following: the function will count how many letters are same in a row, then write the letter and the number of times only.
    # input: String to compress.
    # output: Returns the compressed string.

    if len(st) == 0:
        return ""

    count = 0
    first = st[0]
    for letter in st:
        if letter == first:
            count += 1
        else:
            break
    return first + str(count) + str(CompressString(st[count:]))

def main():
	# Main example:

    toCompress = "aaaaccccccbbedddd"
    result = CompressString(toCompress)
    print(result)

if __name__ == '__main__':
    main()