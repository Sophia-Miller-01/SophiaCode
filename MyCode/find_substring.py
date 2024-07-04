# find_substring.py
def find_substring(s, sub):
    return s.find(sub)

if __name__ == "__main__":
    s = input("Enter the main string: ")
    sub = input("Enter the substring: ")
    index = find_substring(s, sub)
    if index != -1:
        print(f"Substring found at index {index}")
    else:
        print("Substring not found")
