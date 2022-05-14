import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 15)
print(rect.get_area())
rect.set_width(4)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(10)
print(sq.get_area())
sq.set_side(3)
print(sq.get_diagonal())
print(sq)


# Run unit tests automatically
main(module='test_module', exit=False)