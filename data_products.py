import requests
import json

url = "http://localhost:8000/api/products/"

products = [
  {
    "id": 1,
    "name": "Ração para cachorro",
    "price": 50,
    "minimum": 10,
    "amount_per_package": 2,
    "max_availability": 50000
  },
  {
    "id": 2,
    "name": "Ração para coelho",
    "price": 30,
    "minimum": 2,
    "amount_per_package": 2,
    "max_availability": 70000
  },
  {
    "id": 3,
    "name": "Refrigerante",
    "price": 1,
    "minimum": 120,
    "amount_per_package": 12,
    "max_availability": 150000
  },
  {
    "id": 4,
    "name": "Feijão preto",
    "price": 4,
    "minimum": 24,
    "amount_per_package": 12,
    "max_availability": 12000
  },
  {
    "id": 5,
    "name": "Feijão carioca",
    "price": 6,
    "minimum": 24,
    "amount_per_package": 12,
    "max_availability": 12000
  },
  {
    "id": 6,
    "name": "Arroz agulha",
    "price": 4,
    "minimum": 40,
    "amount_per_package": 10,
    "max_availability": 300
  },
  {
    "id": 7,
    "name": "Ração para gato",
    "price": 50,
    "minimum": 40,
    "amount_per_package": 7,
    "max_availability": 50000
  },
  {
    "id": 8,
    "name": "Pão de forma",
    "price": 4.5,
    "minimum": 200,
    "amount_per_package": 20,
    "max_availability": 400000
  }
]

headers = {
  'Content-Type': 'application/json',
}
for line in products:
    payload = json.dumps(line)
    response = requests.request("POST", url, headers=headers, data=payload)

print("Products have been successfully created")