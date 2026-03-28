def demo_sets() -> None:
    """Demonstrate basic set operations."""
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Set difference (set1 - set2):", set1 - set2)


def demo_dictionaries() -> None:
    """Demonstrate basic dictionary operations."""
    student = {"name": "Alice", "age": 25, "grade": "A"}
    print("\nOriginal student dictionary:")
    for key, value in student.items():
        print(key, value)

    # Add and update entries
    student["subject"] = "Math"
    student["age"] = 32
    print("\nAfter adding 'subject' and updating 'age':")
    print(student)

    # Delete an entry with del
    del student["grade"]
    print("\nAfter deleting 'grade':")
    print(student)

    # Remove an entry with pop
    student.pop("subject")
    print("\nAfter popping 'subject':")
    print(student)


def demo_tuples() -> None:
    """Demonstrate basic tuple usage."""
    colors = ("red", "green", "blue")
    single_item = ("glass",)
    print("\nColors tuple:", colors)
    print("Single-item tuple:", single_item)
    print("First color (colors[0]):", colors[0])
    print("Last color (colors[-1]):", colors[-1])


def demo_lists() -> None:
    """Demonstrate basic list operations."""
    numbers = [1, 2, 3, 4]
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "apple", True]

    print("\nNumbers list:", numbers)
    print("Fruits list:", fruits)
    print("Mixed list:", mixed)

    # Accessing elements
    print("numbers[2]:", numbers[2])
    print("fruits[-1]:", fruits[-1])
    print("mixed[1]:", mixed[1])

    # Adding elements
    fruits.append("orange")
    fruits.insert(1, "grape")
    print("\nAfter append and insert:", fruits)

    # Slicing
    sliced_fruits = fruits[2:4]
    print("Sliced fruits (fruits[2:4]):", sliced_fruits)

    # Removing elements
    fruits.remove("banana")
    print("After removing 'banana':", fruits)

    # Deleting by index
    del fruits[0]
    print("After deleting index 0:", fruits)

    # Popping elements from the end
    fruits.pop()
    fruits.pop()
    print("After popping twice:", fruits)


def main() -> None:
    """Run all data structure demos."""
    print("=== Set example ===")
    demo_sets()

    print("\n=== Dictionary example ===")
    demo_dictionaries()

    print("\n=== Tuple example ===")
    demo_tuples()

    print("\n=== List example ===")
    demo_lists()


if __name__ == "__main__":
    main()