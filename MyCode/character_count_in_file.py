# character_count_in_file.py
def count_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return len(text)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        char_count = count_characters(filename)
        print(f"The file {filename} has {char_count} characters.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
