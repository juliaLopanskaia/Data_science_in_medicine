from datetime import date

class Sklad(object):
    def __init__(self, sklad_number):
        self.tech_list = []
        self.tech_dict = {}
        self.sklad_num = sklad_number

    def take_object(self, tech):
        print(f'sklad{self.sklad_num} takes {tech.__class__.__name__}')
        self.tech_list.append(tech)

    def __str__(self):
        str_list = []
        print(f'sklad{self.sklad_num} has:')
        for tech in self.tech_list:
            str_list.append(f'{tech.__class__.__name__} with cost of {tech.cost}; year {tech.year}')
        return '\n'.join(str_list)

    def give_away(self, tech):
        print(f'sklad{self.sklad_num} gives away {tech.__class__.__name__}')
        self.tech_list.remove(tech)
        return tech

    def form_dict(self):
        self.dict = dict((f'{i.__class__.__name__}, {i.cost}rub, {i.year}year old', self.tech_list.count(i)) for i in self.tech_list)
        print(self.dict)


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

sklad = Sklad(1)
sklad.take_object(printer)
sklad.take_object(xerox)
sklad.take_object(scaner)
print(sklad)
print()

xerox2 = Xerox(1000, 1989)
sklad.take_object(xerox2)
sklad.take_object(xerox)

print(sklad)
sklad.form_dict()
print()

sklad2 = Sklad(2)
sklad2.take_object(sklad.give_away(scaner))
print()
print(sklad)
print()
print(sklad2)
