import datetime as dt

class Calculator:
    def __init__(self,limit):
        self.limit = limit
        self.records = []

    def add_record(self,Record):
        self.records.append(Record)

    def get_today_stats(self):
        return sum([x.amount for x in self.records if x.date == dt.datetime.now().date()]) 

    def get_week_stats(self):
        return sum([x.amount for x in self.records if x.date >= (dt.datetime.now().date() - dt.timedelta(7)) and x.date <= dt.datetime.now().date()])

class CashCalculator(Calculator):
    def __init__(self,limit):
        super().__init__(limit)

    USD_RATE = float(76)
    EURO_RATE = float(82)

    def get_today_cash_remained(self,currency):

        currency_dict = {
            'usd': 'USD',
            'eur': 'Euro',
            'rub': 'руб'
        }

        spend_sum = self.get_today_stats()

        if currency.lower() == "usd": 
            rate = self.USD_RATE
        elif currency.lower() == "eur":
            rate = self.EURO_RATE 
        elif currency.lower() == 'rub':
            rate = 1        
        else: 
            return 'Курс валюты не определен'

        if spend_sum < self.limit:
            return  f'На сегодня осталось {round((self.limit - spend_sum) / rate, 2)} {currency_dict[currency.lower()]}'
        elif spend_sum == self.limit:
            return 'Денег нет, держись'
        elif spend_sum > self.limit:
            return f'Денег нет, держись: твой долг - {round((spend_sum - self.limit) / rate, 2)} {currency_dict[currency.lower()]}'

class CaloriesCalculator(Calculator):
    def __init__(self,limit):
        super().__init__(limit)

    def get_calories_remained(self):

        spend_sum = self.get_today_stats()

        if spend_sum < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {str(self.limit - spend_sum)} кКал'
        else:
            return 'Хватит есть!'

class Record:
    def __init__(self,amount,comment,date=''):

        self.comment = comment

        if amount < 0:
            raise ValueError('Сумма должна быть положительной')
        
        self.amount = amount
        
        if date == '':
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()