
def main():
    print(person)

    # Add new key-value pair
    person["address"] = "123 Main St"

    # Update Age
    person["age"] = 32

    # Remove grade
    if "grade" in person:
        del person["grade"]

    print(person)


if __name__ == "__main__":
    main()