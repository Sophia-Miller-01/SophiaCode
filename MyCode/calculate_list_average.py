# calculate_list_average.py
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    average = calculate_average(numbers)
    print(f"The average is {average}")
