from random import randint 
num=randint(0,1000)
print(num)
k=0
n=int(input("Введите число от 0 до 1000: "))
while True:
        
    if n==num:
        print("Вы выиграли")
        break
    elif n>num and k<10:
        print('Ведите число по меньше')
        k+=1
        print(k)
    elif n<num and k<10:
        print('Введите число по больше')
        k+=1
        print(k)
    if k==10 :
        print("Вы проиграли")
        break
    n=int(input())
