"""
#Given a string and a pattern, write a program to find all occurrences of the pattern in the string
#For example, string = "THIS IS A TEST TEXT", pattern = "TEST"
#Output = Pattern found at index 10
#Example 2, string =  "AABAACAADAABAABA", pattern =  "AABA"
#Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

"""


# using brute force approach, we loop through the entire input array
# Time complexity: O(n^2)
# Space Complexity: O(n)
def pattern_matching(input_string: str, text_pattern):
    pattern_len = len(text_pattern)
    matched_patt_index = []
    # looping through the input string but only the length of input string minus the length of pattern
    #
    flag = True
    for i in range(len(input_string) - pattern_len + 1):  # adding +1 as range exclude the end number
        k = 0
        # loop from i till i + pattern length so if i=0 then upto 4, and if i=1 then upto 5 and so on..
        for j in range(i, i + pattern_len):
            # we initialize k = 0 as k is used to iterate over pattern and hence should always start with 0
            # so we loop through the length of pattern and check if any pattern's letter not equal to input_string's
            # letter. If there is any letter that matches then we set flag = False and break from inner loop
            if text_pattern[k] != input_string[j]:
                flag = False
                break
            # if all pattern matches then we increment k until the length of the loop
            else:
                k += 1
        # after looping through the inner loop, if the Flag is still True then we append the index i which is the start
        # of the input index in the list
        if flag:
            matched_patt_index.append(i)
        # we then set flag back to True
        flag = True

    # if pattern matched list is not empty, we return it
    if matched_patt_index:
        return matched_patt_index
    else:
        return None


string = "AABAACAADAABAABA"
pattern = "AABA"
print(f'Pattern found at {pattern_matching(string, pattern)}')
print(f'Pattern found at {pattern_matching("THIS IS A TEST TEXT", "TEXT")}')
