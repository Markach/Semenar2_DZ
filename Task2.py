# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def find_factorial(value):
    Fact=1
    if N==0 or N==1:
        print('1')
    else:
        list=[]   
        for i in range(1,N+1):
           Fact*=i
           list.append(Fact)
        print(list)

try:
    N = int(input('Input N: '))
    find_factorial(N)
except ValueError:
    print('Input real numbers!')
