# Задача «Длина отрезка»
'''
def distance(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    dst = ((y2 - y1) **2 + (x2 - x1) ** 2) ** 0.5
    return dst

#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())

res = distance(x2=int(input()),y2=int(input()),x1=int(input()),y1=int(input()))
print(res)
'''

# Задача «Отрицательная степень»
'''
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))
'''

# Задача «Числа Фибоначчи»
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(int(input())))
'''

# Високосный год
'''
def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False

year = int(input('Введите год: '))
print(is_year_leap(year))
'''

# Квадрат
'''
def square(a):
    return (4 * a, a * a, a * 2 ** 0.5)

print(square(int(input('Введите сторону: '))))
'''

# Времена года
'''
def season(moth):

    if moth == 12 or moth < 3:
        return 'Зима'
    elif moth > 2 and moth < 6:
        return 'Весна'
    elif moth > 5 and moth < 9:
        return 'Лето'
    else:
        return 'Осень'

year_ = int(input('Введите месяц (Число): '))

if year_ > 0 and year_ <= 12:
    print(season(year_))
else:
    print('Введите значение от 1 до 12!')
'''


# Банковский вклад
'''
def bank(a,years):
    for i in range(years):
        a += (a*0.1)
    return a

a_ = int(input('Введите сумму: '))
years_ = int(input('Введите количество лет: '))
print(bank(a_, years_))
'''

# Простые числа
'''
def is_prime(a):
    if a == 2 or a % 2 != 0:
        for i in range(3, int(a ** 0.5), 2):
            if a % i == 0:
                return False
        return True
    return False

a_ = int(input('Введите число от 0 до 1000: '))

if a_ >= 0 and a_ <= 1000:
    print(is_prime(a_))
else:
    print('Полученное значение не входит в диапозон!')
'''

# Правильная дата
'''
def date(d,m,y):
    if d < 0 or m < 0 or y < 0:
        return False

    moth = [31,28,31,30,31,30,31,31,30,31,30,31]

    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        moth[1]=29

    if m >= 1 and m <= 12:
        if d > 0 and d <= moth[m-1]:
            return True
    return False

d_ = int(input('Введите день: '))
m_ = int(input('Введите месяц: '))
y_ = int(input('Введите год: '))

print(date(d_, m_, y_))
'''

