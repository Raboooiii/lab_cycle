import math
def read():
    a = float(input("Enter the first side = "))
    b = float(input("Enter the second side = "))
    c = float(input("Enter the third side = "))
    return a,b,c
def calculate_area(a,b,c):
    if not is_valid_triangle(a,b,c):
        raise ValueError("Invalid triangle: The sum of any two sides must be greater than the third side.")

    s = (a+b+c) / 2
    area = (s * (s - a) * (s - b) * (s - c))**(1/2)
    return area
def is_valid_triangle(a,b,c):
    return (a + b > c) and (b + c > a) and (a + c > b)

# Read the sides of the first triangle
triangle1_sides = read()

# Calculate the area of the first triangle

area1 = calculate_area(*triangle1_sides)

# Read the sides of the second triangle
triangle2_sides = read()

# Calculate the area of the second triangle
area2 = calculate_area(*triangle2_sides)

# Calculate the total area enclosed by both triangles
total_area = area1 + area2

# Calculate the percentage contribution of each triangle towards the total area
triangle1_contribution = (area1 / total_area) * 100
triangle2_contribution = (area2 / total_area) * 100

# Print the results
print("Area of triangle 1:", area1)
print("Area of triangle 2:", area2)
print("Total area:", total_area)
print("Percentage contribution of triangle 1:", triangle1_contribution, "%")
print("Percentage contribution of triangle 2:", triangle2_contribution, "%")
