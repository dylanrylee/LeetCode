
strs = ["eat","tea","tan","ate","nat","bat"]
hashmap = {}

result = []
for string in strs: 
    sortedString = ''.join(sorted(string))
    if sortedString not in hashmap.keys():
        hashmap[sortedString] = string
    else:
        hashmap[sortedString] += f", {string}"
for value in hashmap.values():
    result.append(value)
print(result)