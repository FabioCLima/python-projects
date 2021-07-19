from random import randint
import turtle


class Point:
    """Definição da classe Point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """Método da classe Point que verifica se um ponto está dentro do
        retangulo.

        Args:
            rectangle ([rectangule]): [Objeto da classe Rectangule que possui
            duas coordenadas Point1, Point2]

        Returns:
            [boolean]: [Retorna um boolean que confirma ou refuta um ponto
            estar contido no Rectangule]
        """
        if rectangle.point1.x < self.x < rectangle.point2.x \
           and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:
    """Uma classe que modela um retangulo apartir de dois pontos."""

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):

        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


# class child of Rectangule class
# herda os atributos e métodos da class parent
class GuiRectangule(Rectangle):

    def draw(self, canvas):
        # Go to a certain Coordinates
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


# Create rectangle object
rectangle = GuiRectangule(Point(randint(0, 400), randint(0, 400)),
                          Point(randint(10, 400), randint(10, 400)))

print(f"Rectangle Coordinates: "
      f"{rectangle.point1.x}, "
      f"{rectangle.point1.y}, and "
      f"{rectangle.point2.x}, "
      f"{rectangle.point2.y}  ")

# Get point and area from user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print(f"Your point was inside rectangle: "
      f"{user_point.falls_in_rectangle(rectangle)}")
print(f"Your area was off by: {rectangle.area()- user_area}")

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
