""" Пользователь делает вклад в размере m рублей сроком на n лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Написать функцию bank, принимающую аргументы m и n, и возвращающую сумму, которая будет на счету пользователя через n лет. """

def bank(m,n):
    procent = 0.1
   # m = int(input("Размер вклада: "))
   # n = int(input("Срок вклада : "))
    summa = int(m*(1+procent)**n)
    return summa
print(bank(m,n))
