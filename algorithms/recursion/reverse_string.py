def reverse_string_iterative(string):
    temp = ""
    # here we loop through from original length of the string - 1 to zero
    # since we're iteration from length of the string, we add the letter from the end of the string to the temp string
    for i in range(len(string) - 1, -1, -1):
        temp += string[i]

    return temp


print(reverse_string_iterative("yoyo mastery"))


def reverse_string_iterative2(string):
    temp = ""
    # here we loop through from zero to original length of the string - 1
    # In each iteration, we keep adding the letter from the end of the string to the temp string
    for i in range(len(string)):
        temp = temp + string[len(string) - i - 1]

    return temp


print(reverse_string_iterative("Algorigthms"))


def reverse_string_iterative3(string):
    original_length = len(string)
    # here we loop through from zero to original length of the string - 1
    # In each iteration, we keep adding the letter from the end of the string to the same string
    # after for loop, we'll have reverse string appended to the original string
    # we simply use substring to get the 2nd half of the string
    for i in range(original_length):
        string = string + string[original_length - i - 1]

    return string[original_length:]


print(reverse_string_iterative3("Data Structure"))


def reverse_string_recursive(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string_recursive(string[1:]) + string[0]


print(reverse_string_recursive("nikhil"))
