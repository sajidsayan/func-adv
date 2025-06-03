fruits = ["Apple Fruit 1KG","Orange Fruit 1KG ","Mango Fruit 1KG"]
prices = ["307 Taka","178 Taka","738 Taka"]

data = {fruits:prices for fruits,prices in zip(fruits,prices)}
print(data)
