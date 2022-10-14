# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
def create_list(dim):
    coordinate=[0]*dim
    for i in range(dim):
        try:
            coordinate[i]=float(input(f'ввведите  {i+1} координату точки: '))
        except:
            print('введите число ')   
    print()         
    return coordinate

N=int(input('N-мерное пространство, введите N: '))  
a= create_list(N)
b= create_list(N)

def find_distance(a, b):
    a1=len(a)
    sum=0
    for i in range(a1):
        sum+=(a[i]-b[i])**2 
        res=sum**0.5   
    return res
    

res1=find_distance(a,b)
print(res1)
