import random

N = int(input("Enter the number of random points to generate: "))
points_inside_circle = 0
total_points = 0

while total_points < N:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2 + y**2 < 1:
        points_inside_circle += 1

    total_points += 1
pi_estimate = 4 * points_inside_circle / N
print(f"Approximation of pi:{pi_estimate:.2f}")