import matplotlib.pyplot as plt


# Функція для генерації сегменту кривої Коха
def koch_segment(x0, y0, x1, y1, depth):
    if depth == 0:
        return [(x0, y0), (x1, y1)]
    else:
        dx = x1 - x0
        dy = y1 - y0

        x2 = x0 + dx / 3
        y2 = y0 + dy / 3
        x3 = 0.5 * (x0 + x1) - (3**0.5 / 6) * (y1 - y0)
        y3 = 0.5 * (y0 + y1) + (3**0.5 / 6) * (x1 - x0)
        x4 = x0 + 2 * dx / 3
        y4 = y0 + 2 * dy / 3

        return (koch_segment(x0, y0, x2, y2, depth - 1) +
                koch_segment(x2, y2, x3, y3, depth - 1) +
                koch_segment(x3, y3, x4, y4, depth - 1) +
                koch_segment(x4, y4, x1, y1, depth - 1))

# Функція для генерації сніжинки Коха
def koch_snowflake(depth):
    points = koch_segment(0, 0, 300, 0, depth)
    points += koch_segment(300, 0, 150, 300 * (3**0.5) / 2, depth)
    points += koch_segment(150, 300 * (3**0.5) / 2, 0, 0, depth)
    return points

# Функція для малювання сніжинки Коха
def plot_snowflake(points):
    x_coords, y_coords = zip(*points)
    plt.figure(figsize=(8, 8))
    plt.plot(x_coords, y_coords, 'b')
    plt.axis('equal')
    plt.show()


# Головна функція
def main():
    recursion_level = int(input("Enter the recursion level: "))
    points = koch_snowflake(recursion_level)
    plot_snowflake(points)





if __name__ == "__main__":
    main()
