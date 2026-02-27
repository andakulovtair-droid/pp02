import json

json_string = '{"name": "Ali", "age": 20}'
data = json.loads(json_string)
print("1) Age:", data["age"])


python_dict = {
    "city": "Almaty",
    "country": "Kazakhstan"
}
json_data = json.dumps(python_dict)
print("2) JSON:", json_data)


print("3)")
print(json.dumps(["apple", "banana"]))
print(json.dumps(100))
print(json.dumps(True))