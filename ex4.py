from datetime import date

class Sklad(object):
    def __init__(self):
        self.tech_list = []

    def take_object(self, other):
        self.tech_list.append(other)

    def __str__(self):
        str_list = []
        for tech in self.tech_list:
            str_list.append(f'{tech.__class__.__name__} with cost of {tech.cost}; year {tech.year}')
        return '\n'.join(str_list)


class OrgTechnica(object):
    def __init__(self, cost, year):
        self.cost = cost
        self.year = year

    @property
    def age(self):
        print(f'the age of {self.__class__.__name__} is {date.today().year - self.year}')


class Printer(OrgTechnica):
    def __init__(self, cost, year):
        super().__init__(cost, year)

    @staticmethod
    def print_pic():
        print('I print a beautiful pic')


class Xerox(OrgTechnica):
    def __init__(self, cost, year):
        super().__init__(cost, year)

    @staticmethod
    def xerox_pic():
        print('I xerox a beautiful pic')

class Scaner(OrgTechnica):
    def __init__(self, cost, year):
        super().__init__(cost, year)

    @staticmethod
    def scaner_pic(document_number):
        print('I scan a beautiful document with number', document_number)


printer = Printer(1200, 1996)
printer.print_pic()
printer.age
print()

xerox = Xerox(12700, 1999)
xerox.xerox_pic()
xerox.age
print()

scaner = Scaner(9000, 2020)
scaner.scaner_pic(55)
scaner.age
print()

sklad = Sklad()
sklad.take_object(printer)
sklad.take_object(xerox)
sklad.take_object(scaner)
print(sklad)
