import math

def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def main():
    radius = 5
    height = 10
    volume = calculate_cylinder_volume(radius, height)
    print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume}")

if __name__ == "__main__":
    main()
