class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.height * self.width

    def __str__(self):
        result = '* ' * self.width + '\n'

        for _ in range(self.height - 2):
            result += '*' + ' ' * (self.width * 2 - 3) + '*\n'

        result += '* ' * self.width
        return result


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def main():
    print('Rectangle Calculator\n')
    while True:
        choice = input('Rectangle or square? (r/s): ').lower()
        if choice == 'r':
            height = int(input('{:<10}: '.format('Height')))
            width = int(input('{:<10}: '.format('Width')))
            r = Rectangle(height, width)
            
            print('{:<10}: {}'.format('Perimeter', r.getPerimeter()))
            print('{:<10}: {}'.format('Area', r.getArea()))
            print(r)
        elif choice == 's':
            side = int(input('{:<10}: '.format('Length')))
            s = Square(side)
            
            print('{:<10}: {}'.format('Perimeter', s.getPerimeter()))
            print('{:<10}: {}'.format('Area', s.getArea()))
            print(s)
        else:
            print('Error: Invalid choice')

        repeat = input('\nContinue? (y/n): ')
        print()
        if repeat == 'n':
            break
    print('Bye!')

if __name__ == "__main__":
    main()