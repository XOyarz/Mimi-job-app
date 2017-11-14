from collections import defaultdict
import string
import os

# Get relative path to file
def path_to_file(fileName):
    base_path = os.path.dirname(__file__)
    path_to_file = os.path.join(base_path, fileName)
    return path_to_file

def get_common_pattern(fileLine):
    # Get an array with letters a-z
    alphabet = list(string.ascii_lowercase)
    commonPattern = []
    listLine = list(fileLine.strip('\n'))
    dictionary = {}
    for i in listLine:
        # If char i has already been mapped in the dictionary,
        # append its value to the new commonPattern array
        if i in dictionary:
            commonPattern.append(dictionary[i])
        # Else add the key-value mapping to the dictionary,
        # append the value to the new array and delete 
        # the value from the alphabet array
        else:
            dictionary[i] = alphabet[0]
            commonPattern.append(dictionary[i]) 
            del alphabet[0]
    pattern = ''.join(commonPattern)
    return pattern

# Sum all values greater than one, because only
# those share the same pattern with at least one
# other word ("friendly words")
def count_friends(dictionary):
    friends = 0
    for value in dictionary.values():
        if value > 1:
            friends += value
    return friends

with open(path_to_file('words.txt')) as f:
    # defaultdict allows one to add key or sum value in one step
    results = defaultdict(int)
    for line in f:
        linePattern = get_common_pattern(line)
        # Add pattern to dictionary if not there, or increase value by 1
        results[linePattern] += 1
print(count_friends(results))
