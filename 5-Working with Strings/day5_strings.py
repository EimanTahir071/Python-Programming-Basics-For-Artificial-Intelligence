

# split()

sentence = "Python is fun"
words = sentence.split()
print(words)

# join()
new_sentence = "|".join(words)
print(new_sentence)


text = "I love Java"
updated_text = text.replace("Java", "Python")
print(updated_text)

messy = "     Hello, World     "
cleaned_text = messy.strip()

if __name__ == "__main__":
    print(messy)
    print(cleaned_text)