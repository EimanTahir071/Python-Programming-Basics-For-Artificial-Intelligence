def is_palindrome(text):
    """
    Return True if `text` is a palindrome after normalization.

    Normalization keeps only alphanumeric characters and compares
    the result in a case-insensitive manner.
    """
    text = "".join(char.casefold() for char in text if char.isalnum())
    return text == text[::-1]

if __name__ == "__main__":
    input_text = input("Enter a string: ")
    if is_palindrome(input_text):
        print(f'"{input_text}" is a palindrome.')
    else:
        print(f'"{input_text}" is not a palindrome.')