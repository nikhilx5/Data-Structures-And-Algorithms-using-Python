def rev_string(input_string):
    reversed_string = ""
    for letter in input_string[::-1]:
        # print(letter)
        reversed_string = reversed_string + letter
    return reversed_string


print(rev_string("My Name is Nikhil"))
