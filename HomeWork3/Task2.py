#Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

def list_doubli(arr):
    doubli=[]
    for el in arr:
        if not el in doubli and arr.count(el)>1:
            doubli.append(el)
    return doubli

list_el=[1,2,4,5,1,1,3,3,4,9,8,7,2,2]
print(list_doubli(list_el))