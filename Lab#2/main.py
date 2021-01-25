from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from prettytable import PrettyTable


def main():
    r = Rectangle("красного", 23, 23)
    c = Circle("зеленого", 23)
    s = Square("жёлтого", 23)
    table = PrettyTable()
    table.field_names = ['Таблица фигур']
    table.add_row([r])
    table.add_row([c])
    table.add_row([s])
    print(table)


if __name__ == "__main__":
    main()