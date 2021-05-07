class Circle:

    """[Circle object that holds area data]

    Returns:
        [float]: [area of the circle ]
    """
    pi = 3.14

    def __init__(self, diameter):

        print(f"New circle with diameter: {diameter}.")


    def area(self, radius):
        """[Circle method for performs area of circle calculation]

        Args:
            radius ([float]): [radius of the circle object]

        Returns:
            [float]: [area of the circle]
        """
        area =  radius ** 2 * Circle.pi
        return area
