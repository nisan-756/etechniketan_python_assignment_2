products = {
    "soap": 50,
    "oil": 200,
    "laptop": 60000,
    "phone": 25000,
    "mouse": 500
}

costliest = max(products, key=products.get)

print("Costliest product is", costliest)