person = {"name": "Alice", "age": 25, "grade": "A"}

print(person)

# Add new key-value pair
person["address"] = "123 Main St"

# Update Age
person["age"] = 32

# Remove grade
person.pop("grade", None)
print(person)