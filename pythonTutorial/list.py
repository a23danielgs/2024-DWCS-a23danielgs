""" dognames = ["Fido","Mierdon","Firulais","Sally"]

dognames.insert(0,"Yamin")
print(dognames)
print(dognames[2])

del(dognames[4])
print(dognames)

dogs = {"Fido":8,"Mierdon":12,"Firulais":4,"Sean":2}
print(dogs)

print(dogs["Mierdon"]) """


words = ["PoGo","Spange","Lie-Fi"]
descriptions = ["Slang for Pokemon Go","To collect spare change","Mathematic definition"]

coolDictionary = {}
for i in range(0,len(words)):
    coolDictionary.update({words[i]:descriptions[i]})

for coolWord,coolDescription in coolDictionary.items():
    print(coolWord+" = "+coolDescription)