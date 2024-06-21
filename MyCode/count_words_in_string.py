# count_words_in_string.py
def count_words(s):
    words = s.split()
    return len(words)

string = "Hello world, welcome to the universe."
word_count = count_words(string)
print(f"String: {string}")
print(f"Word Count: {word_count}")
