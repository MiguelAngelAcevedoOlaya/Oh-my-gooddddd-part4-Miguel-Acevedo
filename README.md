# RETO 4

## PUNTO 1

``` mermaid

classDiagram
    class Shape {
        + vertices: list(Point)
        + edges: list(Line)
        + inner_angles: list(float)
        + is_regular: bool
        + compute_area(self)
        + compute_perimeter(self)
        + compute_inner_angles(self)
    }

    class Point {
        + x: int
        + y: int
        + compute_distance(self, Point)
    }

    class Line {
        + start_point: Point
        + end_point: Point
        + length: float
    }

    class Triangle {
    }

    class Isosceles{
    }

    class Equilateral{
    }

    class Scalene{
    }

    class TriRectangle{
    }

    class Rectangle{
    }

    class Square{
    }

    Shape *-- Line 
    Shape *-- Point
    Triangle <|-- Shape
    Isosceles <|-- Triangle
    Equilateral <|-- Triangle
    Scalene <|-- Triangle
    TriRectangle <|-- Triangle
    Rectangle <|-- Shape
    Square <|-- Rectangle
```

```
class Point:
    # Definition of the Point class
    definition: str = "Abstract geometric entity that represents a location in space."

    # Constructor method for the Point class
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    # Method to move the point to a new location
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    # Method to reset the point to the origin
    def reset(self):
        self.x = 0
        self.y = 0
    
    # Method to calcule the distance of two points
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance

class Line:
    # Constructor method to initialize the Line object with start and end points
    def __init__(self, start, end):
        self.start = start  # Start point of the line
        self.end = end      # End point of the line
        self.length = start.compute_distance(end)


class Square:
    def __init__(self, regular: bool, vertices: list, edges: list, inner_angles: list):
        self.regular = regular
        self.vertices = vertices
        self.edges = edges  # Calculate the length of the points
        self.inner_angles = inner_angles
        self.point = Point() # Call class point
        self.line = Line() # Call class line
    
    def compute_area(self):
        pass
    
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass


```
