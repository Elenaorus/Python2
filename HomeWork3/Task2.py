#Дан список повторяющихся элементов.
#Вернуть список с дублирующимися элементами.
#В результирующем списке не должно быть дубликатов.

list_el=[1,2,4,5,1,1,3,3,4,9,8,7,2,2]
doubli=[]
for el in list_el:
    if not el in doubli and list_el.count(el)>1:
        doubli.append(el)
 


print(doubli)
