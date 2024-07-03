def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(map(lambda x_y: abs(x_y[0] - x_y[1]), zip(p1, p2)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
