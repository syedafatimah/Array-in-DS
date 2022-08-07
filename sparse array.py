#find how many times query appears in the string
from collections import Counter
def sparse(strings, queries):
    store = Counter(strings) #save how many times same strings appear
    result = []
    #Now iterate through queries
    for i in queries:
        result.append(store[i])
    return result

#Driver code
new = sparse(["ab", "bba", "ab", "bb"], ["ab", "bb", "bcc"])
print(new)