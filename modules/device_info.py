SMARTPHONES = {
    "iPhone 12": {"year": 2020, "brand": "Apple"},
    "Galaxy S21": {"year": 2021, "brand": "Samsung"},
    "Redmi Note 10": {"year": 2021, "brand": "Xiaomi"}
}

def device_info(model):
    return SMARTPHONES.get(model, {"error": "Modèle inconnu"})
