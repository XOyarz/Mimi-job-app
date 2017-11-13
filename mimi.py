import string
from collections import defaultdict
import os
results = defaultdict(int)
base_path = '/home/xavier/Desktop/'
filename = 'words.txt'
path_to_file = os.path.join(base_path, filename)


with open(path_to_file) as f:
    for line in f:
        alphabet = list(string.ascii_lowercase)
        commonStructure = []
        listLine = list(line)
        dictio = {}
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
                
        joinedStructure = ''.join(commonStructure)
        results[joinedStructure] += 1

friends = 0
for value in results.values():
    if value > 1:
        friends += value
print(friends)       