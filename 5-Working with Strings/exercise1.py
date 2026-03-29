import re

PUNCT_RE = re.compile(r"[^\w\s]")

def clean_text(text: str) -> str:
    """
    Normalize a string by removing punctuation, collapsing repeated whitespace,
    and converting all characters to lowercase.

    Punctuation is defined as any character that is not a word character
    (letters, digits, underscore) or whitespace per the regex pattern.
    """
    # Remove punctuation
    text = PUNCT_RE.sub("", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

if __name__ == "__main__":
    input_text = "   Hello, World.!!! Welcome to Python, Programming....    "
    cleaned_text = clean_text(input_text)
    print("Cleaned Text: ", cleaned_text)
