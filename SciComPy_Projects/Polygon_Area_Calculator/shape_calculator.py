
# Project available in https://repl.it/@lastlost/boilerplate-polygon-area-calculator#shape_calculator.py

class Rectangle:

    width = 0
    height = 0

    def __init__(self, width, height) :
        self.set_width(width)
        self.set_height(height)
    
    def set_width(self, width) :
        self.width = width
    
    def set_height(self, height) :
        self.height = height

    def get_area(self) :
        area = self.width * self.height
        return area

    def get_perimeter(self) :
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self) :
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self) :
        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        else : 
            string = ""
            for y in range(self.height) :
                for x in range(self.width) :
                    string += "*"
                string += "\n"
            return string
    
    def get_amount_inside(self, shape) :
        no_shape_inside = 0
        if shape.width != shape.height :
            if shape.width > self.width or shape.height > self.height :
                return no_shape_inside
            else :
                no_shape_inside = int(((self.width)/(shape.width)) * ((self.height)/(shape.height)))
                return no_shape_inside
        else :
            if shape.width > self.width :
                return no_shape_inside
            else :
                no_shape_inside = int(((self.width)/(shape.width)) * ((self.height)/(shape.height)))
                return no_shape_inside

    def __str__(self) :
        string = ""
        if self.width != self.height :
            string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
            return string
        else :
            string = "Square(side=" + str(self.width) + ")"
            return string

class Square(Rectangle):

    def __init__(self, side) :
        self.set_side(side)

    def set_side(self , side) :
        self.set_width(side)
        self.set_height(side)
    
    def set_width(self, side) :
        self.width = side
        self.height = side

    def set_height(self, side) :
        self.height = side
        self.width = side
