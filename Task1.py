# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

def find_sum(n):
    suma = 0 
    while n > 0:
       digit = n % 10
       suma = suma + digit
       n = n // 10 
    print("Сумма:", suma)


try:
    N = str(input('Input N: ')) 
    n1= int(N.replace('.', ''))
    find_sum(n1)
except ValueError:
    print('Input real numbers!')
