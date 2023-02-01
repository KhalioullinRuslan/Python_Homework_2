# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

print('Введите количество монеток: ')
amount = int(input())
coins = ''
for i in range(amount):
    coins += str(random.randint(0,1))
print(coins)
tails = 0
for i in range(amount):    
    if int(coins[i]) == 0:
        tails += 1
if tails == amount/2 or tails < amount - tails:
    print(str(tails) + ' раз')
if tails > amount - tails:
    print(str(amount - tails) + ' раз')
