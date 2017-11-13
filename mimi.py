import string
from collections import defaultdict
import os
results = defaultdict(int)
base_path = '/home/xavier/Desktop/'
filename = 'words.txt'
path_to_file = os.path.join(base_path, filename)


with open(path_to_file) as f:
    for line in f:
        # get array with letters a-z
        alphabet = list(string.ascii_lowercase)
        commonStructure = []
        listLine = list(line)
        dictio = {}
        # rewrite the line mapping chars to a-z alphabetically. 
        # Check if key-value are already in dict, else add them.
        for i in listLine:
            if i in dictio:
                commonStructure.append(dictio[i])
            else:
                try:
                    dictio[i] = alphabet[0]
                    commonStructure.append(dictio[i]) 
                    alphabet.pop(0)
                except:
                    pass
        # turn the new mapping into a string and add it to a dictionary
        joinedStructure = ''.join(commonStructure)
        results[joinedStructure] += 1

friends = 0
# Sum the keys which value > 1, the ones with a 'friend'
for value in results.values():
    if value > 1:
        friends += value
print(friends)       
