# func_py_vowel_counter.py

def func_py_vowel_counter(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def test_vowel_counter():
    sentences = [
        "Hello world",
        "Python programming",
        "This is a test sentence",
        "Data Science and AI",
    ]
    for sentence in sentences:
        print(f"Vowel count in '{sentence}': {func_py_vowel_counter(sentence)}")

if __name__ == "__main__":
    test_vowel_counter()
