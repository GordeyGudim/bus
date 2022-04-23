#Принимает количество чилиндренов
countOfChildren = int(input())
#Принимает количество фазеров
countOfman = int(input())
#Принимает кол-во мест
count = int(input())
# Сажает фазеров
while countOfman >= 3:
    countOfman -= 3
    count+=20
    count-=3
# Суммирует оставшихся фазеров и чилиндренов и проверяет можно их довести или нет
countOfman += countOfChildren
if countOfman <= count:
    print('Yes')
else:
    print('No')