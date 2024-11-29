class Person:
    def __init__(self,name,email,telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"name:{self.name}    email:{self.email}    telephone:{self.telephone}"
    
class Product:
    def __init__(self,name,description,price,image):
        self.name = name
        self.description = description
        self.price = price
        self.image = image

    def getPrice (self):
        return self.price

    def __str__(self):
        return f"name:{self.name}    description:{self.image}   price:{self.price}    image:{self.image}"

class Order:
    def __init__(self,date,products,client):
        self.date = date
        self.products = products
        self.client = client

    def getTotal(self):
        precio_total = 0
        for product in self.products:
            precio_total = precio_total+product.getPrice()
        return f"{precio_total}€"

    def __str__(self):
        product_str = ""
        for product in self.products:
            product_str+="\n"+str(product)
        return f"date:{self.date}\nproducts:{product_str}\nclient = ({self.client})\nTOTAL={self.getTotal()}"

products = [Product("Kinder","Ta bueno",4,"Kinder.jpg"),Product("Escoba","Ta limpia",10,"Escoba.jpg"),Product("Funda","Pa el movil",3,"Funda.png")]
order1 = Order("29 de nov",products,Person("Daniel","blabla@gmail.com",111222333444))
print(f"{order1}")