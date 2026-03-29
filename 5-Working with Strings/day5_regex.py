"""Demonstrate basic regular expressions: findall to extract digit groups
and sub to mask each digit in a string."""
import re

if __name__ == "__main__":
    text = "Contact me at 123-456-7890"
    digits = re.findall(r"\d+", text)
    print("Digit groups found with re.findall:", digits)

    updated_text = re.sub(r"\d", "X", text)
    print("Text with all digits masked using re.sub:", updated_text)
