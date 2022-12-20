# Реализуйте алгоритм перемешивания списка.

#a = [1,2,3,4,5,6,7,8,9]
# import random
# random.shuffle(a)
# print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

import datetime

def random_num(max_num):    #9
    random_num = datetime.datetime.now().microsecond/(10**6)
    print(random_num)
    return random_num*max_num

for i in range(len(a)-1, -1, -1):
    j = int(random_num(i+1))    # 
    print(j)
    a[i], a[j] = a[j], a[i]
print(a)

    
