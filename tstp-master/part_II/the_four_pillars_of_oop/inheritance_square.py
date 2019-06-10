

class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


class Square(Shape):
    pass

a_square = Square(20,20)
a_square.print_size()
