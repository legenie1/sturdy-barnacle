def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(p1[i] - p2[i]) for i in range(len(p1)))

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
