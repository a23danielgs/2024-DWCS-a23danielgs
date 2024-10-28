words = ["List","Dictionary","Array"]
descriptions = ["Ordered array of objects","Unordered array of key-value pairs","Mathematic definition"]

coolDictionary = {}

for i in range(0,len(words)):
    coolDictionary.update({words[i]:descriptions[i]})

print("The contents of the dictionary are:")
for coolWord,coolDescription in coolDictionary.items():
    print(" "+coolWord+": "+coolDescription)
