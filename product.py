#shop and product, exersice 5
import json

product_data = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1500,
        "quantity": 5
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 50,
        "quantity": 20
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 120,
        "quantity": 10
    }
]


with open("products.json", "w") as f:
    json.dump(product_data, f, indent=2)

with open("products.json", "r") as f:
    products = json.load(f)
    for ch in products:
        
        if ch['price'] > 100 :
            print(ch)
    
    