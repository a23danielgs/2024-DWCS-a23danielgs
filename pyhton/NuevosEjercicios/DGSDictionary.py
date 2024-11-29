def showDictionay (dictionary):
    for key,value in dictionary.items():
        print(f"key:{key}       value:{value}")
    
def findValue (search,dict):
    for key,value in dict.items():
        if (key==search):
            print(f"The value with key = {key} is {value}")

def mergeDictionaries (dict1,dict2):
    for key,value in dict2.items():
        dict1.update({key:value})
    return dict1

products = { 0: "potatoes", 1: "tomatoes", 3: "onions", 4: "garlic" }
showDictionay(products)
products.update({2:"green beans",5:"limes"})
findValue(2,products)
new = mergeDictionaries(products,{6:"cherries",7:"water",8:"paper"})
showDictionay(new)