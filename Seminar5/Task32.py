# Задача No33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

mass=[1,2,3,4,5,5,4,3,2]
mn=min(mass)
mx=max(mass)
for e in range(len(mass)):
    if mass[e]==mx:
        mass[e]=mn
print(mass)