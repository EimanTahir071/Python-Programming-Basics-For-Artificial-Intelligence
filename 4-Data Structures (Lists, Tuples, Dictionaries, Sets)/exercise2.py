def main():
    sentence = input("Enter a Sentence: ")

    # Split the sentence into words
    words = sentence.split()

    # Initialize Dictionary
    word_count = {}

    # Count word frequency
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1

    print(word_count)


if __name__ == "__main__":
    main()