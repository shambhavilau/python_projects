import random
import datetime
year = random.randint(1900, 2021)
print(year)


def leap_year(year):
    if year % 400 == 0:
        # print("leap year")
        return True
    elif year % 100 == 0:
        # print("not leap year")
        return False
    elif year % 4 == 0:
        # print("leap year")
        return True
    else:
        # print("not leap year")
        return False


l = False
month = random.randint(1, 12)
birthday = []


def generate_days(l, month, birthday):
    for i in range(50):
        l = leap_year(year)
        if month == 2 and l == True:
            day = random.randint(1, 29)
        elif month == 2 and l == False:
            day = random.randint(1, 28)
        elif month == 7 or month == 8:
            day = random.randint(1, 31)
        elif month %2 != 0 and month < 7:
            day = random.randint(1, 31)
        elif month % 2 != 0 and month > 7:
            day = random.randint(1, 30)
        elif month % 2 ==0 and month >7:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)
        dd = datetime.date(year, month, day)
        day_of_year = dd.timetuple().tm_yday
        birthday.append(day_of_year)
        birthday.sort()


generate_days(l, month, birthday)

print("Birthdays:", birthday)
paradox = []
for i in range(len(birthday)):
    x = birthday.count(birthday[i])
    if x > 1 and birthday[i] not in paradox:
        paradox.append(birthday[i])
        print("Birthday paradox! We have ", x, " people with same birthday on ", birthday[i], " day of the year")
