# Если вначале пользуемся ЗП для покрытия затрат, а уже потом используем подушку.
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

delta = salary - spend
while (money_capital + delta) >= 0:
    spend = spend * (1 + increase)
    delta = salary - spend
    money_capital += delta
    month += 1

print('Проживём',month, 'мес., приоритезируя трату ЗП')

#Если вначале используем подушку безопасности
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
delta = money_capital - spend
while delta >= 0:
    spend = spend * (1 + increase)
    money_capital += salary
    money_capital -= spend
    delta = money_capital - spend
    month += 1

print('Проживём',month, 'мес., если идём во все тяжкие')
