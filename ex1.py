class Data(object):
    """docstring for Data."""
    def __init__(self, date):
        self.date = date

    @classmethod
    def chislo(cls, date):
        return(date.split('-')[0])

    @staticmethod
    def proverka(date):
        chislo = int(date.split('-')[0])
        if chislo > 31 or chislo <= 0:
            raise DateError('неправильное число')
        else:
            print('good chislo')

        month = int(date.split('-')[1])
        if month > 12 or chislo <= 0:
            raise DateError('неправильный месяц')
        else:
            print('good month')

        year = int(date.split('-')[2])
        if year > 2021 or year <= 0:
            raise DateError('неправильный год')
        else:
            print('good year')

class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt



data = Data('13-10-1996')
print(Data.chislo('32-09-1994'))
print(data.chislo('32-09-1994'))
Data.proverka('10-09-2021')
